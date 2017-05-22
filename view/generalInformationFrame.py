from Tkinter import *
from model.configurations import *
from controller.weatherInformation import *


class GeneralInformationFrame(Frame):
    temperature_frame = Frame

    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)

        self.configure(bg=background_color, width=width, height=height)

        self.create_temperature_widget(parent)

        self.grid()

    def create_temperature_widget(self, general_frame):
        self.temperature_frame = Frame(general_frame, bg=background_color)

        temperature_text = "Current temperature: " + str(get_current_temperature())
        temperature_label = Label(self.temperature_frame, text=temperature_text)
        temperature_label.configure(bg=background_color, fg=text_color)

        min_temperature_text = "Minimal temperature: " + str(get_min_temperature())
        min_temperature_label = Label(self.temperature_frame, text=min_temperature_text)
        min_temperature_label.configure(bg=background_color, fg=text_color)

        max_temperature_text = "Maximum temperature: " + str(get_max_temperature())
        max_temperature_label = Label(self.temperature_frame, text=max_temperature_text)
        max_temperature_label.configure(bg=background_color, fg=text_color)

        weather_image = get_image_for_weather()
        weather_image_view = Label(self.temperature_frame, image=weather_image)
        weather_image_view.image = weather_image
        weather_image_view.configure(bg=background_color, width=80, height=80)

        temperature_label.grid(row=0, column=0, rowspan=1, columnspan=1, sticky="nsew")
        min_temperature_label.grid(row=1, column=0, rowspan=1, columnspan=1, sticky="nsew")
        max_temperature_label.grid(row=2, column=0, rowspan=1, columnspan=1, sticky="nsew")
        weather_image_view.grid(row=3, column=0, rowspan=1, columnspan=1)

        self.temperature_frame.grid()
