import json
def getMinHumidity():
    f = open("config.json","r")
    configString = f.read()
    config = json.loads(configString)
    myHumidity = config["minHumidity"]
    print(myHumidity)
    return myHumidity

def getSensorName():
    f = open("config.json","r")
    configString = f.read()
    config = json.loads(configString)
    mySensor = config["sensorName"]
    return mySensor    