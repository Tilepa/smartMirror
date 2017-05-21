from Tkinter import *

class NewsBlockFrame(Frame):
    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)
        self.pack()
        self.configure(bg="blue", width=width, height=height)
        print("news block")