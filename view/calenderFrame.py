from tkinter import *

class CalenderFrame(Frame):
    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)
        self.grid()
        self.configure(bg="brown", width=width, height=height)
        print("kalender")