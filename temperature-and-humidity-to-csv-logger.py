# Written by David Neuy
# Version 0.1.0 @ 03.12.2014
# This script was first published at: http://www.home-automation-community.com/
# You may republish it as is or publish a modified version only when you 
# provide a link to 'http://www.home-automation-community.com/'. 

#install dependency with 'sudo easy_install apscheduler' NOT with 'sudo pip install apscheduler'
import os, sys, Adafruit_DHT, time
from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
import RPi.GPIO as GPIO
import readSettings
import schedule
sensor                       = Adafruit_DHT.AM2302 #DHT11/DHT22/AM2302
pin                          = 4
min_humidity                 = readSettings.getMinHumidity()
max_humidity                 = readSettings.getMaxHumidity()
min_temp                     = readSettings.getMinTemp()
max_temp                     = readSettings.getMaxTemp()
sensor_name                  = readSettings.getSensorName()
hist_temperature_file_path   = "sensor-values/temperature_" + sensor_name + "_log_" + str(date.today().year) + ".csv"
latest_temperature_file_path = "sensor-values/temperature_" + sensor_name + "_latest_value.csv"
hist_humidity_file_path      = "sensor-values/humidity_" + sensor_name + "_log_" + str(date.today().year) + ".csv"
latest_humidity_file_path    = "sensor-values/humidity_" + sensor_name + "_latest_value.csv"
csv_header_temperature       = "timestamp,temperature_in_celsius,temperature_in_fahrenheit\n"
csv_header_humidity          = "timestamp,relative_humidity\n"
csv_entry_format             = "{:%Y-%m-%d %H:%M:%S},{:0.1f}\n"
csv_temp_entry_format        = "{:%Y-%m-%d %H:%M:%S},{:0.1f},{:0.1f}\n"
sec_between_log_entries      = 60
latest_humidity              = 0.0
latest_temperature           = 0.0
latest_temperature_fahrenheit = 0.0
latest_value_datetime        = None
ledpin                       = 17
heatpin                      = 19 
latest_sensor_data           = None



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledpin,GPIO.OUT)
GPIO.setup(heatpin,GPIO.OUT)

class sensorData:
  def __init__(self, temp, humidity, readTime):
    self.tempCelsius = temp
    self.humidity = humidity
    self.readTime = readTime
    self.tempFahrenheit = temp * 9.0 / 5.0 + 32.0 

def write_header(file_handle, csv_header):
  file_handle.write(csv_header)

def write_value(file_handle, datetime, value):
  line = csv_entry_format.format(datetime, value)
  file_handle.write(line)
  file_handle.flush()

def write_value_temp(file_handle, datetime, value, value2):
  line = csv_temp_entry_format.format(datetime, value, value2)
  file_handle.write(line)
  file_handle.flush()  

def open_file_ensure_header(file_path, mode, csv_header):
  f = open(file_path, mode, os.O_NONBLOCK)
  if os.path.getsize(file_path) <= 0:
    write_header(f, csv_header)
  return f

def write_hist_value_callback():
  global min_humidity, max_humidity, min_temp, max_temp
  tom = schedule.tempschedule()
  min_humidity, max_humidity = tom.getScheduleHumidity()  
  min_temp, max_temp = tom.getScheduleTemp()  
  logfile = open("humidity.log", "a", os.O_NONBLOCK)
  logfile.write("Minimum Humidity set to: " + str(min_humidity) + " at " + str(datetime.now()) + "\n")
  logfile.close()  
  write_value_temp(f_hist_temp, latest_value_datetime, latest_temperature, latest_temperature_fahrenheit)
  write_value(f_hist_hum, latest_value_datetime, latest_humidity)

def write_latest_value():
  with open_file_ensure_header(latest_temperature_file_path, 'w', csv_header_temperature) as f_latest_value:  #open and truncate
    write_value_temp(f_latest_value, latest_value_datetime, latest_temperature, latest_temperature_fahrenheit)
  with open_file_ensure_header(latest_humidity_file_path, 'w', csv_header_humidity) as f_latest_value:  #open and truncate
    write_value(f_latest_value, latest_value_datetime, latest_humidity)

f_hist_temp = open_file_ensure_header(hist_temperature_file_path, 'a', csv_header_temperature)
f_hist_hum  = open_file_ensure_header(hist_humidity_file_path, 'a', csv_header_humidity)

print("Ignoring first 2 sensor values to improve quality...")
for x in range(2):
  Adafruit_DHT.read_retry(sensor, pin)

print("Creating interval timer. This step takes almost 2 minutes on the Raspberry Pi...")
#create timer that is called every n seconds, without accumulating delays as when using sleep
scheduler = BackgroundScheduler()
scheduler.add_job(write_hist_value_callback, 'interval', seconds=sec_between_log_entries)
scheduler.start()
print("Started interval timer which will be called the first time in {0} seconds.".format(sec_between_log_entries));

try:
  while True:
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    if hum is not None and temp is not None:
      latest_humidity, latest_temperature = hum, temp
      latest_temperature_fahrenheit = (temp * 9.0 / 5.0) + 32.0
      #print("min humidity from loop: ", min_humidity)
      if hum <= min_humidity:
        GPIO.output(ledpin,GPIO.HIGH)
      elif hum >= max_humidity:
        GPIO.output(ledpin,GPIO.LOW)
      else: 
        GPIO.output(ledpin,GPIO.LOW)
      print("This is the PIN output: " + str(GPIO.input(ledpin)))

      if temp <= min_temp:
        GPIO.output(heatpin, GPIO.HIGH)
      elif temp >= max_temp:
        GPIO.output(heatpin,GPIO.LOW)
      else:
        GPIO.output(heatpin, GPIO.LOW)

      latest_value_datetime = datetime.today()
      latest_sensor_data = sensorData(latest_temperature, latest_humidity, latest_value_datetime)
      write_latest_value()
    time.sleep(10)
except (KeyboardInterrupt, SystemExit):
  scheduler.shutdown()

