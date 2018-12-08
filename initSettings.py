import json

config = dict([('minHumidity',53)])
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
    f.write(json.dumps(config))


