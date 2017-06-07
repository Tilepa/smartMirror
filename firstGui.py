import time
import os
from multiprocessing import Process
from tkinter import *
from view.generalInformationFrame import GeneralInformationFrame
from view.calenderFrame import CalenderFrame
from view.todayTodosFrame import TodayTodosFrame
from view.newsBlockFrame import NewsBlockFrame

terminate_time = False

class Application(Tk):
    generalInformation = GeneralInformationFrame
    newsBlockFrame = NewsBlockFrame
    todayTodosFrame = TodayTodosFrame
    kalenderFrame = CalenderFrame

    padding = 10
    countColumns = 2
    countRows = 3

    def __init__(self, master):
        Tk.__init__(self)
        master.configure(background="black")

        widthGI = self.winfo_screenwidth() / self.countColumns
        heightGeneral = self.winfo_screenheight() / self.countRows
        widthNBF = self.winfo_screenwidth()
        widthTDF = widthGI
        widthKF = self.winfo_screenwidth()

        self.generalInformation = GeneralInformationFrame(master, width=widthGI, height=heightGeneral)
        self.newsBlockFrame = NewsBlockFrame(master, width=widthNBF, height=heightGeneral)
        self.todayTodosFrame = TodayTodosFrame(master, width=widthTDF, height=heightGeneral)
        self.kalenderFrame = CalenderFrame(master, width=widthKF, height=heightGeneral)

        self.generalInformation.grid(row=0, column=0, rowspan=1, columnspan=1, sticky="nsew")
        self.todayTodosFrame.grid(row=0, column=1, rowspan=1, columnspan=1, sticky="nsew")
        self.newsBlockFrame.grid(row=1, column=0, rowspan=1, columnspan=2, sticky="nsew")
        self.kalenderFrame.grid(row=2, column=0, rowspan=1, columnspan=2, sticky="nsew")

def update_time():
    # while True:
        if terminate_time == False:
            application.generalInformation.update_time(time.strftime("%H:%M"), time.strftime("%S"), time.strftime("%A, %d. %B %Y"))

def update_weather():
    application.generalInformation.update_weather_icon()



if __name__ == "__main__":
    root = Tk()
    root.title("Smart Mirror")
    root.overrideredirect(0)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    application = Application(root)
    update_time()
    # update_weather()
    # p_time = Process(target=update_time())
    # p_time.start()
    # p_time.join()
    root.mainloop()
