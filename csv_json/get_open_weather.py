''' getting weather from openweathermap.org based on command line args
    it takes up to a couple hours for the API key to become active
    free accounts are limited to a small number of APIs: https://openweathermap.org/price
    api docs at https://openweathermap.org/api
    to command line: python3 get_open_weather.py 30.266666 -97.733330 hourly,minutely,alerts
    this is HEAVILY modified from the automate the boring stuff assignment
    How to translate weather ids and icons into usable things:
        ids: https://openweathermap.org/weather-conditions#How-to-get-icon-URL (for current_weather["weather"][0]["id"])
        icons: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2 (for current_weather["weather"][0]["icon"])
    attempted to set up structure to allow different weather data to be returned via different inputs at a later date
'''

import json, requests, sys
from datetime import datetime
from secret import open_weather_appid

def main():
    lat, lon, exclude = command_line_input()
    weather_data = get_weather_data(lat, lon, exclude)
    for key,value in weather_data.items():
        print(str(key) + ': ' + str(value))
    return(weather_data)

def command_line_input():
    # exit if you don't get three arguments in variable assignment nex
    if len(sys.argv) < 3:
        print('Command should be: python3 get_open_weather.py lat lon exclude')
        sys.exit()

    # latitude and longitude + which types of data to exclude: current,minutely hourly daily alerts
    arg1, arg2, arg3 = str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3])

    return arg1, arg2, arg3

# converts meteorological degrees to a cardinal direction
def degrees_to_cardinal(degrees):
    '''
    napproximate conversion of meterological degrees to cardinal direction for wind
    '''
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    ix = int((degrees + 11.25)/22.5 - 0.02)
    return directions[ix % 16]

# performs request.get for weather data and returns a dict with formatted data '''

def get_weather_data(lat, lon, exclude):
    
    # creating url variable with sys.args added to query string + specifying imperial units
    url = 'https://api.openweathermap.org/data/2.5/onecall?units=imperial&lat=%s&lon=%s&exclude=%s&appid=%s' % (lat, lon, exclude, open_weather_appid)

    response = requests.get(url)
    response.raise_for_status()

    # formats json into python data structures
    python_response = json.loads(response.text)

    # picking out current weather only
    current_weather = python_response["current"]

    # formatting strings for human readability
    current_weather["dt"] = datetime.fromtimestamp(current_weather["dt"]).strftime('%m/%d/%Y %I:%M %p')
    current_weather["sunrise"] = datetime.fromtimestamp(current_weather["sunrise"]).strftime('%I:%M %p')
    current_weather["sunset"] = datetime.fromtimestamp(current_weather["sunset"]).strftime('%I:%M %p')
    current_weather["temp"] = str(current_weather["temp"]) + u"\N{DEGREE SIGN}" + 'F'
    current_weather["feels_like"] = str(round(current_weather["feels_like"], 1)) + u"\N{DEGREE SIGN}" + 'F'
    current_weather["pressure"] = str(current_weather["pressure"]) + ' hPa (millibars)'
    current_weather["humidity"] = str(current_weather["humidity"]) + '%'
    current_weather["dew_point"] = str(round(current_weather["dew_point"], 1)) + u"\N{DEGREE SIGN}" + 'F'
    current_weather["clouds"] = str(current_weather["clouds"]) + '%'
    visibility_miles = current_weather["visibility"] / 1609.34 #convert to feet/miles
    current_weather["visibility"] = str(round(visibility_miles, 1)) + ' miles' 
    current_weather["wind_speed"] = str(round(current_weather["wind_speed"], 1)) +  ' mph'
    current_weather["wind_deg"] = str(degrees_to_cardinal(current_weather["wind_deg"]))

    # adding summary values in current_weather["weather"][0] to current weather dict
    summary = current_weather["weather"][0]
    current_weather["main"] = summary["main"]
    current_weather["description"] = summary["description"]
    current_weather["id"] = summary["id"]
    current_weather["icon"] = summary["icon"]

    # and removing current_weather["weather"] from the dict
    current_weather.pop("weather", None)

    return current_weather

main()
