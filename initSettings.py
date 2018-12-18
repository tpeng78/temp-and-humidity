import json

config = dict([('minHumidity',53),('maxHumidity',55),('sensorName','kids-room')])
try: 
    f = open("config.json","x")
    print("config.json does not exist, loading defaults...") 
    f.write(json.dumps(config))
except FileExistsError:
    print("config.json exists")
    minHumidity = input("What's the minimum humidity? ")
    f = open("config.json","w")
    try:
        float(minHumidity)
    except ValueError:
        print("That's not a number.")
        exit
    config["minHumidity"] = minHumidity

    maxHumidity = input("What's the maximum humidity? ")
    try:
        float(maxHumidity)
    except ValueError:
        print("That's not a number.")
        exit
    config["maxHumidity"] = maxHumidity


    f.write(json.dumps(config))


