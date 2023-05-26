# readOpenWeatherMapForecast
Simple Python code to read the free-tier Weather Forecast from the OpenWeatherMap using their published API. This script is also part of the MBA project composing the designed solution with adding the 8 days weather forecast to the data process.

**Note:** This code is the initial version with still room for improvement. Some details are still hardocoded just as a matter of speeding up the development process. 

### Source
https://openweathermap.org/api

### Usage
```
PS C:\dev\WeatherForecast> $Env:OpenWeatherKey = "your-api-key"
PS C:\dev\WeatherForecast> python .\getOpenWeatherForecast.py
```

Besides dumping the result, the script will output the data into a CSV file as follows:
```
readDateTime,geo,forecastDate,probability,precipitation,temperature
2023-05-26 14:15:29,"-23.640191343339424,-46.97599934011645",2023-05-26,0,0.0,25.16
2023-05-26 14:15:29,"-23.640191343339424,-46.97599934011645",2023-05-27,0,0.0,24.7
2023-05-26 14:15:29,"-23.640191343339424,-46.97599934011645",2023-05-28,100,5.12,24.2
2023-05-26 14:15:29,"-23.640191343339424,-46.97599934011645",2023-05-29,84,1.72,14.62
2023-05-26 14:15:29,"-23.640191343339424,-46.97599934011645",2023-05-30,75,1.66,14.31
2023-05-26 14:15:29,"-23.640191343339424,-46.97599934011645",2023-05-31,100,19.31,15.58
2023-05-26 14:15:29,"-23.640191343339424,-46.97599934011645",2023-06-01,48,1.89,13.61
2023-05-26 14:15:29,"-23.640191343339424,-46.97599934011645",2023-06-02,33,0.25,17.79
``` 
