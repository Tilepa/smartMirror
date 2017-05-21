from Tkinter import *
from model.configurations import *
from controller.weatherInformation import *


class GeneralInformationFrame(Frame):
    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)

        self.configure(bg=background_color, width=width, height=height)

        self.temperature_frame = Frame(parent, bg=background_color)
        self.create_temperature_widget()
        self.temperature_frame.grid()

    def create_temperature_widget(self):
        temperature_label = Label(self.temperature_frame, text=get_current_temperature())
        temperature_label.configure(bg=background_color, fg=text_color)
        temperature_label.grid()
