import time
import _thread
from tkinter import *
from controller.weatherInformation import *
from controller.googleAccess import *
from controller.positions import *
from PIL import Image
from PIL import ImageTk


class GeneralInformationFrame(Frame):
    temperature_frame = Frame

    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)
        # TEMP_WIDGET: Frame zur Bündelung der Elemente
        self.temperature_frame = Frame(parent, bg=background_color)
        self.configure(bg=background_color, width=width, height=height)

        self.var_current_time = StringVar()     # Variable für Uhreit
        self.var_seconds = StringVar()          # Variable für Sekunden
        self.var_current_date = StringVar()     # Variable fürs Datum
        # self.weather_image = Image()

        # TIME: Frame für die Zeitanzeige, bestehend aus zwei Labels. Eins für die Minuten und Stunden und das andre für die Sekunden.
        time_frame = Frame(self.temperature_frame, bg=background_color)

        current_time_label = Label(time_frame, textvariable=self.var_current_time)
        current_time_label.configure(bg=background_color, fg=text_color, font=(font_type, 60))
        current_time_label.pack(side=LEFT)

        seconds_label = Label(time_frame, textvariable=self.var_seconds)
        seconds_label.configure(bg=background_color, fg="gray", font=(font_type, 25))
        seconds_label.pack(anchor=W, side=TOP)

        time_frame.pack(anchor=W)

        # DATE: Label für die Anzeige des Datums im Format (TTT, TT. MMM YYYY)
        current_date_label = Label(self.temperature_frame, textvariable=self.var_current_date)
        current_date_label.configure(bg=background_color, fg=text_color, font=(font_type, 25))
        current_date_label.pack(anchor=W)

        # TEMP_AND_ICON: Label für die Anzeige der aktuellen Temperatur, abhaengig vom Standort und Einbindung des Wetter Icons.
        temp_frame = Frame(self.temperature_frame, bg=background_color)

        #path = os.getcwd() + "\weathericons\\" + get_icon_name() + ".jpg"
        path = os.getcwd() + "\weathericons\\01d.jpg"
        weather_image = ImageTk.PhotoImage(Image.open(path))
        self.weather_image_view = Label(temp_frame, image=weather_image, bg="white", width=60, height=60, border=0)
        self.weather_image_view.image = weather_image
        self.weather_image_view.pack(side=LEFT)

        pos = get_city_country()
        temperature_label = Label(temp_frame, text=(pos[0] + ", " + str(round(get_current_temperature(), 1)) + "°C"))
        temperature_label.configure(bg=background_color, fg=text_color, font=(font_type, 15))
        temperature_label.pack(anchor=CENTER, ipadx=10, side=LEFT, fill=X)

        temp_frame.pack(anchor=W)

        # ROOM_TEMP: Label für die Anzeige der Raumtemperatur. Wert vom Sensor.
        roomtemperature_label = Label(self.temperature_frame, text=("Raumtemperatur: ??°C"))
        roomtemperature_label.configure(bg=background_color, fg=text_color, font=(font_type, 10))
        roomtemperature_label.pack(anchor=W)

        # MIN_TEMP: Label für die Anzeige der minimalen Tagestemperatur. Abhaengig vom Standort.
        min_temperature_label = Label(self.temperature_frame, text=("Min: " + str(get_min_temperature()) + "°C"))
        min_temperature_label.configure(bg=background_color, fg=text_color, font=(font_type, 10))
        min_temperature_label.pack(anchor=W)

        # MAX_TEMP: Label für die Anzeige der miximalen Tagestemperatur. Abhaengig vom Standort.
        max_temperature_label = Label(self.temperature_frame, text=("Max: " + str(get_max_temperature()) + "°C"))
        max_temperature_label.configure(bg=background_color, fg=text_color, font=(font_type, 10))
        max_temperature_label.pack(anchor=W)

        # Das Sammelframe wird in parent eingegliedert
        self.temperature_frame.grid()

    def update_time(self, time, seconds, date):
        self.var_current_time.set(time)
        self.var_seconds.set(seconds)
        self.var_current_date.set(date)

    def update_weather_icon(self):
        new_path = os.getcwd() + "\weathericons\\" + get_icon_name() + ".jpg"
        new_weather_image = ImageTk.PhotoImage(Image.open(new_path))
        self.weather_image_view.config(image=new_weather_image)
        self.weather_image_view.image = new_weather_image

