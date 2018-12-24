import json
import re

def cleanTempScale( inputTempScale ):
    myTempScale = str(inputTempScale)
    myTempScale = myTempScale.upper()

    if len(myTempScale) == 1:
        if myTempScale == 'C' or myTempScale == 'F':
            return myTempScale
    elif len(myTempScale) == 0:
        myTempScale = 'C'
    elif len(myTempScale) >= 1:
        if re.search("CEL", myTempScale) != None:
            # allow for misspellings
            myTempScale = 'C'
        elif re.search("FAH", myTempScale)!= None:
            # allow for misspellings
            myTempScale = 'F'
        else:
            myTempScale = 'C' #default to Celsius
        
    return myTempScale

def main():     
    tempscale = 'C'  # C for Celsius or F for Fahrenheit

    config = dict([('minHumidity',53.0),('maxHumidity',55.0),('sensorName','kids-room'), ('mode','simple'), ('maxTemp', 24.0), ('minTemp',20.0),('tempscale','C')])


    try: 
        f = open("config.json","x")
        print("config.json does not exist, loading defaults...") 
        f.write(json.dumps(config,indent=4, sort_keys=True))
    except FileExistsError:
        print("config.json exists")


        tempscale = input("What temperature scale do you want to use Celsius? or Fahrenheit?")
        tempscale = cleanTempScale(tempscale)
        print("Ok! using " + tempscale)
        config["tempscale"] = tempscale 


        mode = input("What mode do you want to run? simple, schedule or daynight?")
        config["mode"] = mode
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


        f.write(json.dumps(config, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()



