import requests
import os 
from datetime import datetime

def weath(city):

    userapi='43edb3af4f6aae98e32c715cdc87b8dc'
    location=city

    complete_api="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+userapi
    #complete_api="https://pro.openweathermap.org/data/2.5/forecast/hourly?q="+location+"&appid="+userapi

    apilink=requests.get(complete_api)
    apidata=apilink.json()
    print("apidata",apidata)
    #print(apidata)
    if apidata['cod']=='404':
        print("Invalid",location)


    else:
    
        temp=round(((apidata['main']['temp'])-273.15),2)
        weather_desc=apidata['weather'][0]['description']
        humidty=apidata['main']['humidity']
        pressure=round(apidata['main']['pressure'],2)
        feels=apidata['main']['feels_like']
        min_temp=round((apidata['main']['temp_min']-273.15),2)
        max_temp=round(apidata['main']['temp_max']-273.15,2)
        wind_speed=round(apidata['wind']['speed'],2)
        #country=apidata['sys']['country']
        data=[temp,pressure,humidty,weather_desc,feels,wind_speed, min_temp,max_temp]

        return data




