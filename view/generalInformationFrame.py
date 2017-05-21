from Tkinter import *
from controller.weatherInformation import *


class GeneralInformationFrame(Frame):
    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)

        self.configure(bg="yellow", width=width, height=height)
        print(get_temperature())
