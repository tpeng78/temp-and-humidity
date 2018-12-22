import json
def getMinHumidity():
    f = open("config.json","r")
    configString = f.read()
    config = json.loads(configString)
    myHumidity = config["minHumidity"]
    try:
        myHumidity = float(myHumidity)
    except ValueError:
        print("This is not a float. Check your config file.\n")
        exit
    return myHumidity

def getMaxHumidity():
    f = open("config.json","r")
    configString = f.read()
    config = json.loads(configString)
    maxHumidity = config["maxHumidity"]
    try:
        maxHumidity = float(maxHumidity)
    except ValueError:
        print("This is not a float. Check your config file.\n")
        exit
    return maxHumidity


def getMinTemp():
    f = open("config.json","r")
    configString = f.read()
    config = json.loads(configString)
    minTemp = config["minTemp"]
    try:
        minTemp = float(minTemp)
    except ValueError:
        print("This is not a float. Check your config file.\n")
        exit
    return minTemp        

def getMaxTemp():
    f = open("config.json","r")
    configString = f.read()
    config = json.loads(configString)
    maxTemp = config["maxTemp"]
    try:
        maxTemp = float(maxTemp)
    except ValueError:
        print("This is not a float. Check your config file.\n")
        exit
    return maxTemp     

def getSensorName():
    f = open("config.json","r")
    configString = f.read()
    config = json.loads(configString)
    mySensor = config["sensorName"]
    return mySensor    