import time
from tkinter import *
from controller.weatherInformation import *
from controller.googleAccess import *
from controller.positions import *
from PIL import Image
from PIL import ImageTk

from view.components.seperator import Seperator
from view.components.weatherForecastComponent import WeatherForecastComponent


class GeneralInformationFrame(Frame):
    temperature_frame = Frame

    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)
        self.configure(bg=background_color, width=width, height=height, padx=50, pady=40)

        # TIME: Frame für die Zeitanzeige, bestehend aus zwei Labels. Eins für die Minuten und Stunden und das andre für die Sekunden.
        time_frame = Frame(self, bg=background_color)

        self.current_time_label = Label(time_frame)
        self.current_time_label.configure(bg=background_color, fg=text_color, font=(font_type, 60))
        self.current_time_label.grid(row=0, column=0, sticky="nw")

        self.seconds_label = Label(time_frame)
        self.seconds_label.configure(bg=background_color, fg=text_color, font=(font_type, 25))
        self.seconds_label.grid(row=0, column=1, sticky="nw")

        # DATE: Label für die Anzeige des Datums im Format (TTT, TT. MMM YYYY)
        self.current_date_label = Label(time_frame)
        self.current_date_label.configure(bg=background_color, fg=text_color, font=(font_type, 25))
        self.current_date_label.grid(row=1, column=0, columnspan=2, sticky="nsew")

        time_frame.grid(row=0, column=0)

        seperator = Seperator(self, height=50)
        seperator.grid(row=1, column=0)

        self.temperature_frame = Frame(self, bg=background_color)

        actual_weather_label = Label(self.temperature_frame, text="aktuelles Wetter:")
        actual_weather_label.configure(bg=background_color, fg=text_color, font=(font_type, 20))
        actual_weather_label.grid(row=0, column=0, sticky="new")

        weather_component = Frame(self.temperature_frame, bg=background_color)

        self.image_actual_weather = get_weather_image()

        self.actual_weather_image_view = Label(weather_component, width=60, height=60, image=self.image_actual_weather)
        self.actual_weather_image_view.image = self.image_actual_weather
        self.actual_weather_image_view.configure(bg=background_color, fg=text_color)
        self.actual_weather_image_view.grid(row=0, column=0, rowspan=3)

        self.actual_weather_temperature = Label(weather_component)
        self.actual_weather_temperature.configure(bg=background_color, fg=text_color, font=(font_type, 25))
        self.actual_weather_temperature.grid(row=0, column=1, columnspan=2, sticky="nse")

        actual_weather_min_label = Label(weather_component, text="min: ")
        actual_weather_min_label.configure(bg=background_color, fg=text_color, font=(font_type, 15))
        actual_weather_min_label.grid(row=1, column=1, sticky="nsew")

        actual_weather_max_label = Label(weather_component, text="max: ")
        actual_weather_max_label.configure(bg=background_color, fg=text_color, font=(font_type, 15))
        actual_weather_max_label.grid(row=2, column=1, sticky="nsew")

        self.actual_weather_min_temperature = Label(weather_component)
        self.actual_weather_min_temperature.configure(bg=background_color, fg=text_color, font=(font_type, 15))
        self.actual_weather_min_temperature.grid(row=1, column=2, sticky="nsew")

        self.actual_weather_max_temperature = Label(weather_component)
        self.actual_weather_max_temperature.configure(bg=background_color, fg=text_color, font=(font_type, 15))
        self.actual_weather_max_temperature.grid(row=2, column=2, sticky="nsew")

        weather_component.grid(row=0, column=1)

        forecast_frame = Frame(self.temperature_frame, bg=background_color, pady=30)

        self.forecast_component_one = WeatherForecastComponent(parent=forecast_frame, day=1)
        self.forecast_component_one.configure(padx=10)
        self.forecast_component_one.grid(row=0, column=0)

        self.forecast_component_two = WeatherForecastComponent(parent=forecast_frame, day=2)
        self.forecast_component_two.configure(padx=10)
        self.forecast_component_two.grid(row=0, column=1)

        self.forecast_component_three = WeatherForecastComponent(parent=forecast_frame, day=3)
        self.forecast_component_three.configure(padx=10)
        self.forecast_component_three.grid(row=0, column=2)

        forecast_frame.grid(row=1, column=0, columnspan=2)

        # Das Sammelframe wird in parent eingegliedert
        self.temperature_frame.grid(row=2, column=0)

        self.update_time()
        self.update_weather()
        self.update_weather_image()

    def update_time(self):
        new_date = time.strftime("%d/%m/%Y")
        new_time = time.strftime('%H:%M')
        new_seconds = time.strftime("%S")

        if new_time != self.current_time_label.__getitem__("text"):
            self.current_time_label.configure(text=new_time)
        if new_date != self.current_date_label.__getitem__("text"):
            self.current_date_label.configure(text=new_date)
        if new_seconds != self.seconds_label.__getitem__("text"):
            self.seconds_label.configure(text=new_seconds)

        self.after(200, self.update_time)

    def update_weather(self):
        new_temp = str(get_current_temperature()) + "°C"
        new_temp_min = str(get_min_temperature()) + "°C"
        new_temp_max = str(get_max_temperature()) + "°C"

        if new_temp != self.actual_weather_temperature.__getitem__("text"):
            self.actual_weather_temperature.configure(text=new_temp)
        if new_temp_min != self.actual_weather_min_temperature.__getitem__("text"):
            self.actual_weather_min_temperature.configure(text=new_temp_min)
        if new_temp_max != self.actual_weather_max_temperature.__getitem__("text"):
            self.actual_weather_max_temperature.configure(text=new_temp_max)

        self.after(360000, self.update_weather)

    def update_weather_image(self):
        self.image_actual_weather = get_weather_image()
        self.actual_weather_image_view.configure(image=self.image_actual_weather)
        self.actual_weather_image_view.image = self.image_actual_weather

        self.after(360000, self.update_weather_image)

