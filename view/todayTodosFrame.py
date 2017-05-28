from tkinter import *

class TodayTodosFrame(Frame):
    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)
        self.pack()
        self.configure(bg="green", width="400", height="400")
        print("today todos")