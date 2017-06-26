import os
from sys import platform

from model.configurations import pin_of_tempsensor, default_return_error

if platform == "linux" or platform == "linux2":
    import Adafruit_DHT


def get_actual_temperature():
    if platform == "linux" or platform == "linux2":
        # linux
        sensor = Adafruit_DHT.DHT11
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_of_tempsensor)
        return temperature + ", " + humidity
    else:
        return default_return_error
