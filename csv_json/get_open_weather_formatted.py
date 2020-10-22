''' getting weather from openweathermap.org based on command line args and
    prints formatted data
    example on command line:
    python3 get_open_weather_formatted.py 30.266666 -97.733330 minutely,hourly
    API docs: https://openweathermap.org/api
'''

import json
import requests
import sys
import pprint
from datetime import datetime
from secret import open_weather_appid


def command_line_input():
    # exit if you don't get three arguments in variable assignment
    if len(sys.argv) < 3:
        print('Command should be: python3 get_open_weather.py lat lon exclude')
        sys.exit()

    # latitude and longitude + which types of data to exclude:a
    # current,minutely hourly daily alerts
    arg1, arg2, arg3 = str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3])

    return arg1, arg2, arg3


# converts meteorological degrees to a cardinal direction
def degrees_to_cardinal(degrees):

    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                  "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    ix = int((degrees + 11.25)/22.5 - 0.02)
    return directions[ix % 16]


# standardized temperature output
def format_temp(temp):
    temp = str(round(temp, 1)) + u"\N{DEGREE SIGN}" + 'F'
    return temp


# formats current weather data
def format_weather_data(weather):

    header = 'Austin Weather'
    
    # converting to month/day/year & 12-hr time
    date = str(datetime.fromtimestamp(
        weather["dt"]).strftime('%m/%d/%Y %I:%M %p'))
    
    # rounds and adds degree symbol + Fahrenheit
    temp = format_temp(weather["temp"])
    feels_like = format_temp(weather["feels_like"])
    temps = str('Temp: ' + temp + '    ' + 'Feels Like: ' + feels_like)

    # convert feet to miles, round
    visibility = 'Visibility: ' + str(round(weather["visibility"] / 1609.34, 1)) + ' miles'

    sunrise = datetime.fromtimestamp(weather["sunrise"]).strftime('%I:%M %p')
    sunset = datetime.fromtimestamp(weather["sunset"]).strftime('%I:%M %p')
    sun = str('Sunrise: ' + sunrise + '     ' + 'Sunset: ' + sunset)
    
    pressure = 'Pressure: ' + str(weather["pressure"]) + ' hPa (millibars)'
    humidity = 'Humidity: ' + str(weather["humidity"]) + '%'
    dew_point = 'Dew point: ' + format_temp(weather["dew_point"])

    wind_speed = str(round(weather["wind_speed"], 1)) + ' mph'
    wind_deg = str(degrees_to_cardinal(weather["wind_deg"]))
    wind = str('Winds: ' + wind_deg + ' ' + wind_speed)

    description = weather["weather"][0]["description"].title()
    
    ordered_current = [header,
                       date,
                       description,
                       temps,
                       sun,
                       wind,
                       pressure,
                       humidity,
                       dew_point,
                       visibility,
                      ]

    return ordered_current


# performs request.get for weather data and returns a dict with formatted data
def get_weather(lat, lon, exclude):

    # creating url with sys.args added to query+ specifying imperial units
    url = 'https://api.openweathermap.org/data/2.5/onecall?units=imperial&lat=%s&lon=%s&exclude=%s&appid=%s' % (lat, lon, exclude, open_weather_appid)

    response = requests.get(url)
    response.raise_for_status()

    # formats json into python data structures
    current_weather_data = json.loads(response.text)["current"]
  
    return current_weather_data


def display_weather(weather):

    vertical_separator = '-' * 42
    string_width = 40

    for item in weather:
        print(vertical_separator)
        print('|' + str(item).center(string_width, ' ') + '|')

    print(vertical_separator)

            
def main():
    
    lat, lon, exclude = command_line_input()
    current_weather_data = get_weather(lat, lon, exclude)

    try:
        formatted_current = format_weather_data(current_weather_data)
        display_weather(formatted_current)
    
    except:
        print('Skipping current weather.')
        pass


main()
