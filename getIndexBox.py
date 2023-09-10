import asyncio
import aiohttp
import ssl
import utils
import numpy as np
import os
import json
import time as tm

top =    49.384
right = -66.888
bottom = 24.546
left = -124.731

startDate = "2023-04-01"
endDate = "2050-12-31"
desiredVariables = ["temperature_2m_max", "shortwave_radiation_sum", "rain_sum"]
models=['EC_Earth3P_HR']

modelString = ",".join(models)
dailyVariablesString = ",".join(desiredVariables)

url_list = []
latitude = top

while (latitude > bottom):
    longitude = left
    while (longitude < right):
        latitudeS = float(latitude)
        longitudeS = float(longitude)
        url_list.append(f'https://climate-api.open-meteo.com/v1/climate?latitude={latitudeS}&longitude={longitudeS}&start_date={startDate}&end_date={endDate}&models={modelString}&daily={dailyVariablesString}')
        longitude += 0.5
    latitude -= 0.125


async def fetch(session, url):
    async with session.get(url, ssl=ssl.SSLContext()) as response:
        return await response.json()


async def fetch_all(urls, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        results = await asyncio.gather(*[fetch(session, url) for url in urls], return_exceptions=True)
        return results



loop = asyncio.get_event_loop()
urls = url_list
htmls = loop.run_until_complete(fetch_all(urls, loop))
print("done")





top =    49.384297
right = -66.888932
bottom = 24.546337
left = -124.731077

startTime = "2023-04-01"
endTime = "2050-12-31"
desiredVariables = ["temperature_2m_max", "shortwave_radiation_sum", "rain_sum"]

finalDict = {2023: [],
             2024: [],
             2025: [],
             2026: [],
             2027: [],
             2028: [],
             2029: [],
             2030: [],
             2031: [],
             2032: [],
             2033: [],
             2034: [],
             2035: [],
             2036: [],
             2037: [],
             2038: [],
             2039: [],
             2040: [],
             2041: [],
             2042: [],
             2043: [],
             2044: [],
             2045: [],
             2046: [],
             2047: [],
             2048: [],
             2049: [],
             2050: []}


latitude = top

predictedParticleValues = []
for year in range(2023, 2051):
    predictedParticleValues.append(utils.predictParticle(year))

masterKey = 0

while (latitude > bottom):
    longitude = left
    for key in finalDict:
        finalDict[key].append([])
    currentYear = 2023
    while (longitude < right):
        #print(f'Latitude :{latitude}')
        #print(f'Longitude :{longitude}')
        
        finalIndex = []
        
        summerTempDataIndex = 0
        summerRadiationIndex = 0
        summerRainIndex = 0
        winterTempDataIndex = 0
        winterRadiationIndex = 0
        winterRainIndex = 0
        tempData = []
        radiationData = []
        rainData = []

        summerDataProcessed = False
        winterDataProcessed = False
        
        #climateData = utils.getClimateChangeData(latitude, longitude, startTime, endTime, desiredVariables)
        climateData = htmls[masterKey]
        masterKey += 1
        try:
            for i, time in enumerate(climateData['daily']['time']):
                break
        except:
            climateData = utils.getClimateChangeData(latitude, longitude, startTime, endTime, desiredVariables)
        for i, time in enumerate(climateData['daily']['time']):
            year = int(time[:4])
            match time[5:7]:
                case "07":
                    #print("here1")
                    tempData.append(climateData['daily']['temperature_2m_max'][i])
                    radiationData.append(climateData['daily']["shortwave_radiation_sum"][i])
                    rainData.append(climateData['daily']['rain_sum'][i])
                case "06":
                    #print("here2")
                    tempData.append(climateData['daily']['temperature_2m_max'][i])
                    radiationData.append(climateData['daily']["shortwave_radiation_sum"][i])
                    rainData.append(climateData['daily']['rain_sum'][i])
                    summerDataProcessed = False
                case "08":
                    #print("here3")
                    if not (summerDataProcessed):
                        summerTempDataIdex = utils.getTempIndex(tempData)
                        summerRadiationIndex = utils.getRadiationIndex(radiationData)
                        summerRainIndex = utils.getRainIndex(rainData)
                        
                        tempData.clear()
                        radiationData.clear()
                        rainData.clear()
                        
                        summerDataProcessed = True
                case "12":
                    #print("here4")
                    tempData.append(climateData['daily']['temperature_2m_max'][i])
                    radiationData.append(climateData['daily']["shortwave_radiation_sum"][i])
                    rainData.append(climateData['daily']['rain_sum'][i])
                    winterDataProcessed = False
                    if time == "2050-12-31":
                        winterTempDataIndex = utils.getTempIndex(tempData)
                        winterRadiationIndex = utils.getRadiationIndex(radiationData)
                        winterRainIndex = utils.getRainIndex(rainData)

                        tempData.clear()
                        radiationData.clear()
                        rainData.clear()
                        
                        winterDataProcessed = True

                        finalTempIndex = max(summerTempDataIndex, winterTempDataIndex)
                        finalRadiationIndex = max(summerRadiationIndex, winterRadiationIndex)
                        finalRainIndex = max(summerRainIndex, winterRainIndex)


                        #print("\nAppending Values\n")
                        finalIndex.append(utils.getTotalIndex(predictedParticleValues[year - 2023], finalTempIndex, finalRadiationIndex, finalRainIndex))
                case "01":
                    #print("here5")
                    if not (winterDataProcessed):
                        winterTempDataIndex = utils.getTempIndex(tempData)
                        winterRadiationIndex = utils.getRadiationIndex(radiationData)
                        winterRainIndex = utils.getRainIndex(rainData)

                        tempData.clear()
                        radiationData.clear()
                        rainData.clear()
                        
                        winterDataProcessed = True

                        finalTempIndex = max(summerTempDataIndex, winterTempDataIndex)
                        finalRadiationIndex = max(summerRadiationIndex, winterRadiationIndex)
                        finalRainIndex = max(summerRainIndex, winterRainIndex)

                        #print("\nAppending Values\n")
                        finalIndex.append(utils.getTotalIndex(predictedParticleValues[year - 2023], finalTempIndex, finalRadiationIndex, finalRainIndex))

        #print(finalIndex)
        for i, value in enumerate(finalIndex):
            finalDict[currentYear + i][-1].append(value)
            #print(latitude, longitude, currentYear + 1)
        longitude += 0.5
    latitude -= 0.125

#print(str(finalDict[2023]))
    print("done")

with open(r"C:\Users\Eppat\Documents\Personal\HackDuke\sampleEvenLargerFile.json", "w") as out_file:
    json.dump(finalDict, out_file)
