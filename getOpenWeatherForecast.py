from datetime import datetime
import pandas as pd 
import pytz 
import requests
import time
import sys 
import os

# OpenWeatherMap API Key
#
api_key = os.getenv('OpenWeatherKey')

# MBA Test Location (harcoded)
#
read_lat = '-23.640191343339424'
read_lon = '-46.97599934011645'
filename = 'output/weatherForecastAsOf-%s.csv' % datetime.now(tz=pytz.timezone('America/Sao_Paulo')).strftime('%Y%m%d%H%M%S')

def getData():

    # Anhangá (MBA Project Test Location)
    #
    endpoint = 'https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric' % (
                read_lat, 
                read_lon, 
                api_key
    )

    # HTTP Request
    #
    response = requests.get(endpoint)
    if response.status_code != 200:
        print('Failed!') 
        sys.exit(1)
    else:
        #
        # Normal flow

        df = pd.DataFrame()
        data = response.json()

        readDateTime = datetime.now(tz=pytz.timezone('America/Sao_Paulo')).strftime('%Y-%m-%d %H:%M:%S')
        geo = ','.join([read_lat,read_lon])

        for day in data['daily']:
            dayDict = {}
            forecastDate = time.strftime('%Y-%m-%d', time.localtime(day['dt']))
            probability = day['pop']
            temperatura = day['temp']['day']
            if 'rain' in day:
                volume = day['rain']
            else:
                volume = 0

            dayDict['readDateTime'] = readDateTime
            dayDict['geo'] = geo 
            dayDict['forecastDate'] = forecastDate 
            dayDict['probability'] = int(probability*100)
            dayDict['precipitation'] = volume 
            dayDict['temperature'] = temperatura

            tempDF = pd.DataFrame([dayDict])
            df = pd.concat([df, tempDF]) #append has been deprecated

        df.to_csv(filename, index=False)
        print(df.head(10))
        sys.exit(0)

if __name__ == '__main__':
    getData()