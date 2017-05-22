import base64
import urllib

import cStringIO
import pyowm
from PIL import Image
from PIL import ImageTk

from positions import *

api_key = '4731b498cb45d327e16017ec7f843eb1'


def get_weather():
    position = get_lat_long()

    weather_api = pyowm.OWM(api_key)

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
    encoded_string = cStringIO.StringIO(request)
    image = Image.open(encoded_string).convert("RGB")
    photo = ImageTk.PhotoImage(image)

    return photo


