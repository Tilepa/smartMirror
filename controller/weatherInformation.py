import os
from sys import platform

import pyowm
import io
from PIL import Image, ImageTk

from controller.positions import *
from model.weather import Weather

API_KEY = '4731b498cb45d327e16017ec7f843eb1'


def get_weather():
    position = get_lat_long()
    weather_api = pyowm.OWM(API_KEY)
    current_weather = weather_api.weather_at_coords(lat=position[0], lon=position[1]).get_weather()
    return current_weather


def get_current_temperature():
    temperature = get_weather().get_temperature("celsius")
    return temperature["temp"]


def get_max_temperature():
    temperature = get_weather().get_temperature("celsius")
    return temperature["temp_max"]


def get_min_temperature():
    temperature = get_weather().get_temperature("celsius")
    return temperature["temp_min"]


def get_image_for_weather():
    weather = get_weather()
    weather_icon_name = weather.get_weather_icon_name()
    url = "http://openweathermap.org/img/w/" + weather_icon_name + ".png"
    request = requests.get(url).content
    encoded_string = io.BytesIO(request)
    image = Image.open(encoded_string).convert("RGB")
    photo = ImageTk.PhotoImage(image)
    return photo


def get_icon_name():
    return get_weather().get_weather_icon_name()


def get_forecast(day):
    weather_api = pyowm.OWM(API_KEY)
    fc = weather_api.daily_forecast('Dortmund,de', limit=day)
    forecast = fc.get_forecast()
    list_weathers = forecast.get_weathers()

    weather = list_weathers[day - 1]
    temperature = weather.get_temperature("celsius")
    return Weather(temperature["min"], temperature["max"], weather.get_weather_icon_name())


def get_weather_image(image_name=""):

    if image_name == "":
        icon_name = get_icon_name()
    else:
        icon_name = image_name

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
