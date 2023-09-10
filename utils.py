import urllib.request
import json
import time
from global_land_mask import globe
import pandas as pd
import math


def getClimateChangeData(latitude, longitude, startDate, endDate, dailyVariables, models=['EC_Earth3P_HR']):
    ''' This function uses the desired lat, long, daily variables, and other params to form
        the url, then sends a request to open-metro, who returns the string of a json,
        which can be directly translated to a python list

        @param latitude the latitude of the desired point as a decimal
        @param longitude the longitude of the desired point as a decimal
        @param startDate the date of the beginning of the data in format YYYY-MM-DD
        @param endDate the date of the end of the data in format YYYY-MM-DD
        @param dailyVariables the names as strings of all the desired daily variables found at open-metro
        @param models a list of the models from which data is pulled (auto-set if not specified)

        @return newDict a python dictionary with all requested data. Output format is found at open-metro
    '''
    
    modelString = ",".join(models)
    dailyVariablesString = ",".join(dailyVariables)

    latitude = float(latitude)
    longitude = float(longitude)
    
    url = f'https://climate-api.open-meteo.com/v1/climate?latitude={latitude}&longitude={longitude}&start_date={startDate}&end_date={endDate}&models={modelString}&daily={dailyVariablesString}'
    print(url)
    #url = r"https://climate-api.open-meteo.com/v1/climate?latitude=52.52&longitude=13.41&start_date=2016-06-16&end_date=2016-06-17&models=MRI_AGCM3_2_S,EC_Earth3P_HR&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&daily=temperature_2m_max,shortwave_radiation_sum"
    
    page = urllib.request.urlopen(url)
    newDict = json.loads(page.read())

    return newDict

def isLand(lat, long):
    return globa.is_land(lat, long)

def getParticleData():
    data = pd.read_csv(r"C:\Users\Eppat\Documents\Personal\HackDuke\EXP_PM2_5_09092023180509395")
    #for name in data["

def predictParticle(year):
    return 19.6581 - 3.04027*(year - 1990)**0.204337 ## This equation is the best fit nth power line for the given data for pm2.5

def getParticleIndex(particle):
    expectedParticle = 5
    if (particle <= expectedParticle):
        return 0
    return math.sqrt( 0.5 * (particle - expectedParticle) / (expectedParticle*0.1536) ) ## 0.1536 is the standard deviation

def getTempIndex(temp):
    temp = [i for i in temp if i is not None]
    length = len(temp)
    if (length == 0):
        return 0
    average = sum(temp) / length
    average = sum(temp) / len(temp)
    if (average > 80):
        return math.sqrt(average - 80)
    elif (average < 36):
        return math.sqrt(36 - average)
    else:
        return 0

def getRainIndex(rain):
    expectedAverage = 0.5
    rain = [i for i in rain if i is not None]
    length = len(rain)
    if (length == 0):
        return 0
    else:
        average = sum(rain) / length
        std = abs((average - expectedAverage) / expectedAverage)
        return math.sqrt(std)

def getRadiationIndex(radiation):
    radiation = [i for i in radiation if i is not None]
    length = len(radiation)
    if (length == 0):
        return 0
    average = sum(radiation) / length
    radiationAmount = average * 1000000 / 3600
    if radiationAmount <= 100:
        return 0
    else:
        return math.sqrt(radiationAmount/100)

def getTotalIndex(particleIndex, tempIndex, radiationIndex, rainIndex):
    total = particleIndex + tempIndex + radiationIndex + rainIndex
    total *= 2
    totalNew = 100 / (1 + math.exp(-0.3*(total-54)))#((100 / (1 + math.exp(-0.85*(total-54)))) - 55)**2 +55
    return totalNew ## Since the max total of each of these should be 10, multiplying it by 2.5 gives us a range from 0 - 100

##particleIndex = getParticleIndex(0)
##tempIndex = getTempIndex([50])
##radiationIndex = getRadiationIndex([0])
##rainIndex = getRainIndex([0.5])
##
##particleIndex = getParticleIndex(60)
##tempIndex = getTempIndex([100])
##radiationIndex = getRadiationIndex([50])
##rainIndex = getRainIndex([19])

#print(getTotalIndex(particleIndex, tempIndex, radiationIndex, rainIndex))
    

##start = time.time()
##print(time.time() - start)
##print(getClimateChangeData("a", "a", "a", "a", "a", "a"))
##print(time.time() - start)
