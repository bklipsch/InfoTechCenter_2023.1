print("************************************************************************")
print("Gasoline Branch\n\n")

# Import Libraries Here
import random
from time import sleep

# Function that lists Gas Stations, randomly choosing one, and return its value
def gasLevelGuage():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Function with a list of GasStations
def listOfGasStation():
    gasStations = ["Shell","Speedway","Exxon","Meijer","Costco","marathon","BP","Circle K","Westco"]
    gasStationsNearby = random .choice(gasStations)
    return gasStationsNearby

# Function will call the gasLevelGauge to determine gas level and find a close gas station if low
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50), 1)
    gasLevelIndicator = gasLevelGuage()
    if gasLevelIndicator == "Empty":
        print("****WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.")
        sleep(1.5)
        print("The closest gas station is",listOfGasStation(),"which is",milesToGasStationsLow, milesToGasStationsLow,"miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a Quarter Tank, checking Google Maps for the closest gas station.")
        sleep(1.5)
        print("The closest gas station is",listOfGasStation(),"which is",milesToGasStationsQuarterTank,"miles away")
    elif gasLevelIndicator == "Half tank":
        print("Your gas tank has a half of a tank which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at three quarter tank!")
    else:
        print("Your gas tank is full - Yeah! - Congratulation! - Vroom Vroom")


gasLevelAlert()
