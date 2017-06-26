import os
from sys import platform

import pyowm
from PIL import Image, ImageTk

from controller.positions import *
from model.configurations import default_icon_name, default_return_error, WEATHER_API_KEY
from model.weather import Weather


def get_weather():
    try:
        position = get_lat_long()
        weather_api = pyowm.OWM(WEATHER_API_KEY)
        current_weather = weather_api.weather_at_coords(lat=position[0], lon=position[1]).get_weather()
        return current_weather
    except:
        return default_return_error


def get_current_temperature():
    try:
        temperature = get_weather().get_temperature("celsius")
        return temperature["temp"]
    except:
        return default_return_error


def get_max_temperature():
    try:
        temperature = get_weather().get_temperature("celsius")
        return temperature["temp_max"]
    except:
        return default_return_error


def get_min_temperature():
    try:
        temperature = get_weather().get_temperature("celsius")
        return temperature["temp_min"]
    except:
        return default_return_error


def get_icon_name():
    try:
        return get_weather().get_weather_icon_name()
    except:
        return default_return_error


def get_forecast(day):
    try:
        weather_api = pyowm.OWM(WEATHER_API_KEY)
        fc = weather_api.daily_forecast('Dortmund,de', limit=day)
        forecast = fc.get_forecast()
        list_weathers = forecast.get_weathers()

        weather = list_weathers[day - 1]
        temperature = weather.get_temperature("celsius")
        return Weather(temperature["min"], temperature["max"], weather.get_weather_icon_name())
    except:
        return Weather(default_return_error, default_return_error, default_icon_name)


def get_weather_image(image_name=""):
    try:
        if image_name == "":
            icon_name = get_icon_name()
            if icon_name == default_return_error:
                icon_name = default_icon_name
        else:
            icon_name = image_name
    except:
        icon_name = default_icon_name

    if platform == "linux" or platform == "linux2":
        # linux
        path = os.getcwd() + "/weathericons/" + icon_name + ".jpg"
    elif platform == "darwin":
        # MAC OS X
        path = os.getcwd() + "/weathericons/" + icon_name + ".jpg"
    elif platform == "win32":
        # Windows
        path = os.getcwd() + "\\weathericons\\" + icon_name + ".jpg"

    image = Image.open(path)
    image = image.resize((60, 60), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(width=60, height=60, image=image, format="jpg")

    return photo
