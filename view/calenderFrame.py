from tkinter import *
from model.configurations import *

class CalenderFrame(Frame):
    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)
        self.configure(bg=background_color, width=width, height=height)
        print("kalender")