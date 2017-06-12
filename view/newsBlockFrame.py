from tkinter import *

from controller.newsfeedAccess import get_news
from model.configurations import *
from view.components.seperator import Seperator


class NewsBlockFrame(Frame):

    news_entries = []
    news_entry_width = 0

    entry_views_frame = Frame()

    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)
        self.configure(bg=background_color, width=width, height=height)
        self.news_entry_width = width - 40

        self.title_label = Label(self, text="News")
        self.title_label.configure(bg=background_color, fg=text_color, font=(font_type, font_title_size))
        self.title_label.grid(row=0, column=0, sticky="w")

        self.show_news()

    def show_news(self):
        self.entry_views_frame = Frame(self)
        self.entry_views_frame.configure(width=self.news_entry_width, padx=20, bg=background_color)
        self.news_entries = get_news(4)

        row = 0

        for news_entry in self.news_entries:
            entry_view = Frame(self.entry_views_frame)
            entry_view.configure(width=self.news_entry_width, bg=background_color)

            title_label = Label(entry_view, text=news_entry.title)
            title_label.configure(font=(font_type, 16), bg=background_color, fg=text_color,
                                  wraplength=self.news_entry_width)
            title_label.grid(row=0, column=0, sticky="nw")

            description_label = Label(entry_view, text=news_entry.description + " ...")
            description_label.configure(font=(font_type, 14), bg=background_color, fg=text_color,
                                        anchor=NW, justify=LEFT, wraplength=self.news_entry_width)
            description_label.grid(row=1, column=0, sticky="nw")

            seperator = Seperator(entry_view)
            seperator.grid(row=2, column=0, sticky="ew")

            entry_view.grid(row=row, column=0, sticky="nsew")
            row += 1

        self.entry_views_frame.grid(row=1, column=0, sticky="nsew")

        self.after(600000, self.show_news)
