import json
import datetime
class scheduleRecord:
    def __init__(self, starttime, endtime, starthour, minHumidity, minTemp):
        self.starttime = starttime
        self.endtime = endtime
        self.starthour = starthour
        self.minHumidity = minHumidity
        self.minTemp = minTemp


class tempschedule:

    def __init__(self):
        self.scheduletype = "hourly"
        self.myschedules=[]
        self.myschedules.append(scheduleRecord(0, datetime.datetime.now().timestamp(), 8, 20, 80)); 
        self.myschedules.append(scheduleRecord(0, datetime.datetime.now().timestamp(), 19, 55, 80)); 
        self.myschedules.append(scheduleRecord(0, datetime.datetime.now().timestamp(), 7, 10, 80)); 
        self.myschedules.append(scheduleRecord(0, datetime.datetime.now().timestamp(), 0, 55, 80));         
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



