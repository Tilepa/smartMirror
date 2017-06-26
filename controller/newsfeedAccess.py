import feedparser

from model.configurations import *
from model.newsfeedEntry import Newsfeed_Entry


#all news entries will returned if count=0
def get_news(count=0):
    news_entry_list = []
    try:
        feed = feedparser.parse(NEWS_URL)

        if count == 0:
            count = len(feed.entries)

        for i in range(0, count):
            entry = feed.entries[i]

            entry_object = Newsfeed_Entry(entry.title, entry.description)
            news_entry_list.append(entry_object)
    except:
        pass

    return news_entry_list