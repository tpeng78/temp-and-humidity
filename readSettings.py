import json
def getMinHumidity():
    f = open("config.json","r")
    configString = f.read()
    config = json.loads(configString)
    myHumidity = config["minHumidity"]
    return myHumidity

def getMaxHumidity():
    f = open("config.json","r")
    configString = f.read()
    config = json.loads(configString)
    maxHumidity = config["maxHumidity"]
    return maxHumidity

def getSensorName():
    f = open("config.json","r")
    configString = f.read()
    config = json.loads(configString)
    mySensor = config["sensorName"]
    return mySensor    