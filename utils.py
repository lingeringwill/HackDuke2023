import urllib.request
import json
import time


def getData(latitude, longitude, startDate, endDate, dailyVariables, models=['CMCC_CM2_VHR4','FGOALS_f3_H','HiRAM_SIT_HR','MRI_AGCM3_2_S','EC_Earth3P_HR','MPI_ESM1_2_XR','NICAM16_8S']):
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
    
    modelString = "".join(models)
    dailyVariablesString = "".join(dailyVariables)
    
    url = r"https://climate-api.open-meteo.com/v1/climate?latitude={latitude}&longitude={longitude}&start_date={startDate}&end_date={endDate}&models={modelString}&daily={dailyVariablesString}"
    
    page = urllib.request.urlopen(url)
    newDict = json.loads(page.read())

    return newDict


