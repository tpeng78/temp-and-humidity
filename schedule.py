import json
import datetime
class scheduleRecord:
    def __init__(self, starttime, endtime, starthour, minHumidity, maxHumidity, minTemp, maxTemp):
        self.starttime = starttime
        self.endtime = endtime
        self.starthour = starthour
        self.minHumidity = minHumidity # at or below this, the humidifier will turn on 
        self.maxHumidity = maxHumidity # at this or above, the humidifier will turn off
        self.minTemp = minTemp # at or below this, the heater will turn on 
        self.maxHumidity = maxHumidity # at or below this, the heater will turn off


class tempschedule:

    def __init__(self):
        self.scheduletype = "hourly"
        self.myschedules=[]
        self.myschedules.append(scheduleRecord(0, datetime.datetime.now().timestamp(), 8, 20, 21, 80, 82)); 
        self.myschedules.append(scheduleRecord(0, datetime.datetime.now().timestamp(), 19, 40, 42, 80, 82)); 
        self.myschedules.append(scheduleRecord(0, datetime.datetime.now().timestamp(), 7, 10, 11, 80, 82)); 
        self.myschedules.append(scheduleRecord(0, datetime.datetime.now().timestamp(), 0, 40, 42, 80, 82));         
        #print("schedule created")
        #for i in self.myschedules:
        #    print (i.starthour)

    def getScheduleHour(self,myscheduleRecord):
        return myscheduleRecord.starthour

    def getScheduleHumidity(self):
        currentTime = datetime.datetime.now()
        timestamp = datetime.datetime.now().timestamp()
        searchTime = datetime.datetime.fromtimestamp(timestamp)

        sortedSchedules = sorted(self.myschedules,key=self.getScheduleHour)
        desiredHumidity = 20 
        for i in sortedSchedules:
            if searchTime.hour >= i.starthour: 
                desiredHumidity = i.minHumidity
            else:
                exit        
        #print("min humidity ", desiredHumidity)
        return desiredHumidity



