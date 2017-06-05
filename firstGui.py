import time
import _thread
import threading
from tkinter import *
from view.generalInformationFrame import GeneralInformationFrame
from view.calenderFrame import CalenderFrame
from view.todayTodosFrame import TodayTodosFrame
from view.newsBlockFrame import NewsBlockFrame


class App(Tk):
    generalInformation = GeneralInformationFrame
    newsBlockFrame = NewsBlockFrame
    todayTodosFrame = TodayTodosFrame
    kalenderFrame = CalenderFrame

    padding = 10
    countColumns = 4
    countRows = 2

    def __init__(self, master):
        Tk.__init__(self)
        master.configure(background="black")

        widthGI = self.winfo_screenwidth() / self.countColumns
        heightGeneral = self.winfo_screenheight() / self.countRows
        widthNBF = self.winfo_screenwidth() / self.countColumns * 2
        widthTDF = widthGI
        widthKF = self.winfo_screenwidth() / self.countColumns * 2

        self.generalInformation = GeneralInformationFrame(master, width=widthGI, height=heightGeneral)
        self.newsBlockFrame = NewsBlockFrame(master, width=widthNBF, height=heightGeneral)
        self.todayTodosFrame = TodayTodosFrame(master, width=widthTDF, height=heightGeneral)
        self.kalenderFrame = CalenderFrame(master, width=widthKF, height=heightGeneral)

        self.generalInformation.grid(row=0, column=0, rowspan=1, columnspan=1, sticky=N+W)
        self.newsBlockFrame.grid(row=0, column=1, rowspan=1, columnspan=2, sticky=N+E+W)
        self.todayTodosFrame.grid(row=0, column=3, rowspan=1, columnspan=1, sticky=N+E)
        self.kalenderFrame.grid(row=1, column=2, rowspan=1, columnspan=2, sticky=N+S+E+W)

        #_thread.start_new_thread(self.update_time(), self)
        #_thread.start_new(self.update_time())
        #thread_time = threading.Thread(target=self.update_time())
        #thread_time.start()

    def update_time(self):
        while True:
            self.generalInformation.update_time()

root = Tk()
root.title("Smart Mirror")
root.overrideredirect(0)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
App(root)
root.mainloop()