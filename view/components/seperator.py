from tkinter import *

from model.configurations import *


def Seperator(master, height=0):
    if height == 0:
        height = seperator_height_invisible
    return Frame(master, relief=SUNKEN, height=height, bg=background_color)


def SeperatorAsLine(master):
    return Frame(master, relief=SUNKEN, height=seperator_height_visible, bg="grey")


def SeperatorCombined(master):
    frame = Frame(master, relief=SUNKEN, bg=background_color)
    seperator1 = SeperatorAsLine(frame)
    seperator2 = Seperator(frame)

    seperator1.pack(fill=BOTH)
    seperator2.pack(fill=BOTH)
    return frame
