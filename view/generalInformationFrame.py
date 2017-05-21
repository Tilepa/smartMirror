from Tkinter import *
from model.configurations import *
from controller.weatherInformation import *


class GeneralInformationFrame(Frame):
    temperature_frame = Frame

    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)

        self.configure(bg=background_color, width=width, height=height)

        self.create_temperature_widget(parent)

    def create_temperature_widget(self, generalFrame):
        self.temperature_frame = Frame(generalFrame, bg=background_color)

        temperature_text = "Current temperature: " + str(get_current_temperature())
        temperature_label = Label(self.temperature_frame, text=temperature_text)
        temperature_label.configure(bg=background_color, fg=text_color)

        min_temperature_text = "Minimal temperature: " + str(get_min_temperature())
        min_temperature_label = Label(self.temperature_frame, text=min_temperature_text)
        min_temperature_label.configure(bg=background_color, fg=text_color)

        max_temperature_text = "Maximum temperature: " + str(get_max_temperature())
        max_temperature_label = Label(self.temperature_frame, text=max_temperature_text)
        max_temperature_label.configure(bg=background_color, fg=text_color)

        temperature_label.grid()
        min_temperature_label.grid()
        max_temperature_label.grid()

        self.temperature_frame.grid()
