import pyowm
from positions import *

api_key = '4731b498cb45d327e16017ec7f843eb1'


def get_temperature():
    position = get_lat_long()

    weather_api = pyowm.OWM(api_key)

    daily_forecast = weather_api.daily_forecast_at_coords(lat=position[0], lon=position[1])
    current_weather = weather_api.weather_at_coords(lat=position[0], lon=position[1]).get_weather()

    return current_weather.get_temperature("celsius")

def get_current_temperature():
    temperature = get_temperature()

    return temperature["temp"]


def get_max_temperature():
    temperature = get_temperature()

    return temperature["temp_max"]


def get_min_temperature():
    temperature = get_temperature()

    return temperature["temp_min"]