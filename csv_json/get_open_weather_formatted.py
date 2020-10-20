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


# formats both daily and current weather data
def format_weather_data(weather, timeframe):

    # formatting strings for human readability
    if timeframe == "current":
        weather["dt"] = datetime.fromtimestamp(
            weather["dt"]).strftime('%m/%d/%Y %I:%M %p')
        weather["temp"] = format_temp(weather["temp"])
        weather["feels_like"] = format_temp(weather["feels_like"])
        visibility_miles = weather["visibility"] / \
            1609.34  # convert to feet/miles
        weather["visibility"] = str(round(visibility_miles, 1)) + ' miles'

    elif timeframe == "day":
        weather["dt"] = datetime.fromtimestamp(
            weather["dt"]).strftime('%m/%d/%Y')
        for time, temp in weather["temp"].items():
            weather["temp"][time] = format_temp(weather["temp"][time])
        for time, temp in weather["feels_like"].items():
            weather["feels_like"][time] = format_temp(
                weather["feels_like"][time])
        weather["pop"] = str("{:.0%}".format(weather["pop"]))

    weather["sunrise"] = datetime.fromtimestamp(
        weather["sunrise"]).strftime('%I:%M %p')
    weather["sunset"] = datetime.fromtimestamp(
        weather["sunset"]).strftime('%I:%M %p')
    weather["pressure"] = str(weather["pressure"]) + ' hPa (millibars)'
    weather["humidity"] = str(weather["humidity"]) + '%'
    weather["dew_point"] = str(
        round(weather["dew_point"], 1)) + u"\N{DEGREE SIGN}" + 'F'
    weather["clouds"] = str(weather["clouds"]) + '%'
    weather["wind_speed"] = str(round(weather["wind_speed"], 1)) + ' mph'
    weather["wind_deg"] = str(degrees_to_cardinal(weather["wind_deg"]))

    # adding summary values in weather["weather"][0] to main weather dict
    summary = weather["weather"][0]
    weather["main"] = summary["main"]
    weather["description"] = summary["description"]
    weather["id"] = summary["id"]
    weather["icon"] = summary["icon"]

    # and removing weather["weather"] from the dict
    weather.pop("weather", None)

    return weather


# performs request.get for weather data and returns a dict with formatted data
def get_weather(lat, lon, exclude):

    # creating url with sys.args added to query+ specifying imperial units
    url = 'https://api.openweathermap.org/data/2.5/onecall?units=imperial&lat=%s&lon=%s&exclude=%s&appid=%s' % (lat, lon, exclude, open_weather_appid)

    response = requests.get(url)
    response.raise_for_status()

    # formats json into python data structures
    python_response = json.loads(response.text)

    formatted_current = {}
    formatted_daily = {}

    try:
        current_weather = python_response["current"]
        formatted_current = format_weather_data(current_weather, "current")
    except:
        pass

    try:
        daily_weather = python_response["daily"]
        formatted_daily = []
        for day in daily_weather:
            formatted_day = format_weather_data(day, 'day')
            formatted_daily.append(formatted_day)
    except:
        pass

    pprint.pprint(formatted_daily)

    return formatted_current, formatted_daily


def main():
    lat, lon, exclude = command_line_input()
    formatted_current, formatted_daily = get_weather(lat, lon, exclude)

    pprint.pprint(formatted_current)

    return(formatted_current, formatted_daily)


main()
