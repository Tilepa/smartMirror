import time
from tkinter import *
from controller.weatherInformation import *
from controller.googleAccess import *
from controller.positions import *
from PIL import Image
from PIL import ImageTk

from view.components.weatherForecastComponent import WeatherForecastComponent


class GeneralInformationFrame(Frame):
    temperature_frame = Frame
    weather_image = ImageTk

    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)
        self.configure(bg=background_color, width=width, height=height)

        # TIME: Frame für die Zeitanzeige, bestehend aus zwei Labels. Eins für die Minuten und Stunden und das andre für die Sekunden.
        time_frame = Frame(self, bg=background_color)

        self.current_time_label = Label(time_frame)
        self.current_time_label.configure(bg=background_color, fg=text_color, font=(font_type, 60))
        self.current_time_label.grid(row=0, column=0, sticky="nw")

        self.seconds_label = Label(time_frame)
        self.seconds_label.configure(bg=background_color, fg=text_color, font=(font_type, 25))
        self.seconds_label.grid(row=0, column=1, sticky="nw")

        time_frame.grid(row=0, column=0)

        # DATE: Label für die Anzeige des Datums im Format (TTT, TT. MMM YYYY)
        self.current_date_label = Label(time_frame)
        self.current_date_label.configure(bg=background_color, fg=text_color, font=(font_type, 25))
        self.current_date_label.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # TEMP_AND_ICON: Label für die Anzeige der aktuellen Temperatur, abhaengig vom Standort und Einbindung des Wetter Icons.
        temp_frame = Frame(self, bg=background_color)

        #path = os.getcwd() + "/weathericons/" + get_icon_name() + ".jpg"
        path = os.getcwd() + "/weathericons/01d.jpg"

        image_file = Image.open(path)
        self.weather_image = ImageTk.PhotoImage(image_file)
        #self.weather_image_view = Label(temp_frame, image=self.weather_image, bg="white", width=60, height=60, border=0)
        #self.weather_image_view.image  = self.weather_image
        #self.weather_image_view.pack(side=LEFT)

        pos = get_city_country()
        temperature_label = Label(temp_frame, text=(pos[0] + ", " + str(round(get_current_temperature(), 1)) + "°C"))
        temperature_label.configure(bg=background_color, fg=text_color, font=(font_type, 15))
        temperature_label.pack(anchor=CENTER, ipadx=10, side=LEFT, fill=X)

        temp_frame.grid(row=1, column=0)

        self.temperature_frame = Frame(self, bg=background_color)

        # ROOM_TEMP: Label für die Anzeige der Raumtemperatur. Wert vom Sensor.
        roomtemperature_label = Label(self.temperature_frame, text=("Raumtemperatur: ??°C"))
        roomtemperature_label.configure(bg=background_color, fg=text_color, font=(font_type, 10))
        roomtemperature_label.grid(row=0, column=0)

        # MIN_TEMP: Label für die Anzeige der minimalen Tagestemperatur. Abhaengig vom Standort.
        min_temperature_label = Label(self.temperature_frame, text=("Min: " + str(get_min_temperature()) + "°C"))
        min_temperature_label.configure(bg=background_color, fg=text_color, font=(font_type, 10))
        min_temperature_label.grid(row=1, column=0)

        # MAX_TEMP: Label für die Anzeige der miximalen Tagestemperatur. Abhaengig vom Standort.
        max_temperature_label = Label(self.temperature_frame, text=("Max: " + str(get_max_temperature()) + "°C"))
        max_temperature_label.configure(bg=background_color, fg=text_color, font=(font_type, 10))
        max_temperature_label.grid(row=2, column=0)

        # Das Sammelframe wird in parent eingegliedert
        self.temperature_frame.grid(row=0, column=1)

        self.forecast_component = WeatherForecastComponent(parent=self.temperature_frame, day=1)
        self.forecast_component.grid(row=3, column=0)

        self.update_time()

    def update_time(self):
        new_date = time.strftime("%d/%m/%Y")
        new_time = time.strftime('%H:%M')
        new_seconds = time.strftime("%S")

        if new_time != self.current_time_label.__getitem__("text"):
            self.current_time_label.configure(text=new_time)
        if new_date != self.current_date_label.__getitem__("text"):
            self.current_date_label.configure(text=new_date)
        if new_seconds != self.seconds_label.__getitem__("text"):
            self.seconds_label.configure(text=new_seconds)

        self.after(200, self.update_time)

    def update_weather_icon(self):
        new_path = os.getcwd() + "/weathericons/" + get_icon_name() + ".jpg"
        new_weather_image = ImageTk.PhotoImage(Image.open(new_path))
        self.weather_image_view.config(image=new_weather_image)
        self.weather_image_view.image = new_weather_image

