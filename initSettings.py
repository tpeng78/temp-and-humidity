import json

config = dict([('minHumidity',53.0),('maxHumidity',55.0),('sensorName','kids-room')])
try: 
    f = open("config.json","x")
    print("config.json does not exist, loading defaults...") 
    f.write(json.dumps(config))
except FileExistsError:
    print("config.json exists")
    minHumidity = input("What's the minimum humidity? ")
    f = open("config.json","w")
    try:
        minHumidity = float(minHumidity)
    except ValueError:
        print("That's not a number.")
        exit
    config["minHumidity"] = minHumidity

    maxHumidity = input("What's the maximum humidity? ")
    try:
        maxHumidity = float(maxHumidity)
    except ValueError:
        print("That's not a number.")
        exit
    config["maxHumidity"] = maxHumidity

    minTemp = input("What's the minimum temperature? ")
    f = open("config.json","w")
    try:
        minTemp = float(minTemp)
    except ValueError:
        print("That's not a number.")
        exit
    config["minTemp"] = minTemp

    maxTemp = input("What's the maximum temperature? ")
    try:
        maxTemp = float(maxTemp)
    except ValueError:
        print("That's not a number.")
        exit
    config["maxTemp"] = maxTemp    


    f.write(json.dumps(config))


