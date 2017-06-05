import time
import _thread
from tkinter import *
from controller.weatherInformation import *
from controller.googleAccess import *
from controller.positions import *




class GeneralInformationFrame(Frame):
    temperature_frame = Frame

    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)
        self.temperature_frame = Frame(parent, bg=background_color)
        self.configure(bg=background_color, width=width, height=height)

        self.var_current_time = StringVar()
        self.var_seconds = StringVar()
        self.var_current_date = StringVar()
        self.var_current_time.set(time.strftime("%H:%M"))
        self.var_seconds.set(time.strftime("%S"))
        self.var_current_date.set(time.strftime("%A, %d. %B %Y"))

        current_time_label = Label(self.temperature_frame, textvariable=self.var_current_time)
        current_time_label.configure(bg=background_color, fg=text_color, font=(font_type, 60))

        seconds_label = Label(self.temperature_frame, textvariable=self.var_seconds)
        seconds_label.configure(bg=background_color, fg="gray", font=(font_type, 25))

        current_date_label = Label(self.temperature_frame, textvariable=self.var_current_date)
        current_date_label.configure(bg=background_color, fg=text_color, font=(font_type, 25))

        pos = get_city_country()
        temperature_label = Label(self.temperature_frame, text=(pos[0] + " " + str(round(get_current_temperature(), 1)) + "°C"))
        temperature_label.configure(bg=background_color, fg=text_color, font=(font_type, 15))

        roomtemperature_label = Label(self.temperature_frame, text=("Raumtemperatur: ??°C"))
        roomtemperature_label.configure(bg=background_color, fg=text_color, font=(font_type, 10))

        min_temperature_label = Label(self.temperature_frame, text=("Min: " + str(get_min_temperature()) + "°C"))
        min_temperature_label.configure(bg=background_color, fg=text_color, font=(font_type, 10))

        max_temperature_label = Label(self.temperature_frame, text=("Max: " + str(get_max_temperature()) + "°C"))
        max_temperature_label.configure(bg=background_color, fg=text_color, font=(font_type, 10))

        weather_image = get_image_for_weather()
        weather_image_view = Label(self.temperature_frame, image=weather_image, bg=background_color, width=80, height=80)
        weather_image_view.image = weather_image

        current_time_label.grid(row=0, column=0, columnspan=2, sticky=W)
        seconds_label.grid(row=0, column=0, columnspan=2, sticky=E+N, padx=100)
        current_date_label.grid(row=1, column=0, rowspan=1, columnspan=1, sticky=W)
        temperature_label.grid(row=2, column=0, rowspan=1, columnspan=1, sticky=W)
        roomtemperature_label.grid(row=3, column=0, sticky=W)
        min_temperature_label.grid(row=4, column=0, rowspan=1, columnspan=1, sticky=W)
        max_temperature_label.grid(row=5, column=0, rowspan=1, columnspan=1, sticky=W)
        weather_image_view.grid(row=6, column=0, rowspan=1, columnspan=1)

        self.temperature_frame.grid()
        self.grid()

    def update_time(self):
        self.var_current_time.set(time.strftime("%H:%M"))
        self.var_current_date.set(time.strftime("%A, %d. %B %Y"))