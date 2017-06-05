import feedparser
from tkinter import *
from model.configurations import *

class NewsBlockFrame(Frame):
    NEWS_URL = "http://feeds.t-online.de/rss/nachrichten"

    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)
        self.configure(bg=background_color, width=width, height=height)
        self.feed = feedparser.parse(self.NEWS_URL)
        self.title_label = Label(self, text="News", bg=background_color, fg=text_color, font=(font_type, 18, "underline"))
        self.feed_text = Text(self, bg=background_color, fg=text_color, font=(font_type, 12), padx=10, pady=10, borderwidth=0)
        self.title_label.grid(row=0, sticky=W)
        self.feed_text.grid(row=1, column=0, sticky=W)
        self.update_text()
        self.grid()

    def update_text(self):
        #entry_frame = Frame(self, bg=background_color, padx=10, pady=10, height=300)
        #r = 0
        count = 1
        for post in self.feed.entries:
            if count > 5:
                pass
            else:
                #title_label = Label(entry_frame, text=post.title, bg=background_color, fg=text_color, font=(font_type, 12, "bold"))
                #feed_text = Text(entry_frame, bg=background_color, fg=text_color, font=(font_type, 12), borderwidth=0)
                #title_label.grid(row=r, columnspan=2, sticky=W)
                #feed_text.grid(row=(r+1), columnspan=2, sticky=W)
                #r += 2

                self.feed_text.insert(END, "(" + str(count) + ") " + post.title + "\n\n")
                #self.feed_text.insert(END, post.description + "\n\n")
                count += 1
        #entry_frame.grid(row=1, column=0, sticky=W)