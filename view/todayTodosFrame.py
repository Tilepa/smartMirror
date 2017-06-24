from tkinter import *
from tkinter import ttk

from controller.googleAccess import *
from model.configurations import *
from view.components.seperator import Seperator, SeperatorAsLine, SeperatorCombined


class TodayTodosFrame(Frame):

    calendarEntries = []

    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)
        self.configure(bg=background_color, width=width, height=height, padx=50)

        self.calendarEntries = get_next_20_calendar_entries()

        title = Label(self, text="Nächste Kalenderereignisse")
        title.configure(font=(font_type, font_title_size), bg=background_color, fg=text_color)#, pady=30, padx=50)
        title.grid(sticky=W)

        self.update_calendar_entries()

    def update_calendar_entries(self):

        row = 1
        for calendarEntry in self.calendarEntries:
            calendar_title = "Titel: " + calendarEntry.title
            start_string = "Start: "
            end_string = "Ende: "
            start_date_string = str(calendarEntry.startDate.strftime("%a: %d/%m/%y-%H:%M"))
            end_date_string = str(calendarEntry.endDate.strftime("%a: %d/%m/%y-%H:%M"))

            entry_frame = Frame(self, bg=background_color)
            entry_frame.configure(padx=10, pady=10)

            title_label = Label(entry_frame, text=calendar_title)
            title_label.configure(font=(font_type, calendar_title_size), bg=background_color, fg=text_color)
            title_label.grid(row=0, column=0, columnspan=2, sticky="nsw")

            start_label = Label(entry_frame, text=start_string)
            start_label.configure(bg=background_color, fg=text_color, font=(font_type, start_end_size))
            start_label.grid(row=1, column=0, sticky="nsw")

            end_label = Label(entry_frame, text=end_string)
            end_label.configure(bg=background_color, fg=text_color, font=(font_type, start_end_size))
            end_label.grid(row=1, column=1, sticky="nsw")

            start_date_label = Label(entry_frame, text=start_date_string)
            start_date_label.configure(bg=background_color, fg=text_color, font=(font_type, start_end_dates_size))
            start_date_label.grid(row=2, column=0, sticky="nsew")

            end_date_label = Label(entry_frame, text=end_date_string)
            end_date_label.configure(bg=background_color, fg=text_color, font=(font_type, start_end_dates_size))
            end_date_label.grid(row=2, column=1, sticky="nsew")

            seperator = Seperator(entry_frame)
            seperator.grid(row=3, column=0, columnspan=2, sticky="ew")

            entry_frame.grid(row=row, column=0, sticky="nsw")
            row += 1

        self.after(calendar_update, self.update_calendar_entries)
