import datetime
from tkinter import *
from controller.weatherInformation import *
from model.configurations import background_color, text_color, font_type, forecast_image_size, actual_extrema_size, \
    forecast_update
from view.components.seperator import SeperatorAsLine


class WeatherForecastComponent(Frame):
    def __init__(self, parent, day):
        Frame.__init__(self, parent)
        self.configure(bg=background_color)
        self.day = day

        self.forecast = get_forecast(self.day)

        time_of_forecast = datetime.datetime.now()
        time_of_forecast = time_of_forecast + datetime.timedelta(days=self.day)

        weekday_label = Label(self, text=time_of_forecast.strftime("%a"))
        weekday_label.configure(bg=background_color, fg=text_color, font=(font_type, 15))
        weekday_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        seperator = SeperatorAsLine(self)
        seperator.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.forecast_image = get_weather_image(image_name=self.forecast.icon_name)

        self.image_label = Label(self, image=self.forecast_image)
        self.image_label.image = self.forecast_image
        self.image_label.configure(bg=background_color, fg=text_color, width=forecast_image_size, height=forecast_image_size)
        self.image_label.grid(row=2, column=0, columnspan=2, sticky="nsew")

        min_text_label = Label(self, text="min")
        min_text_label.configure(bg=background_color, fg=text_color, font=(font_type, actual_extrema_size))
        min_text_label.grid(row=3, column=0, sticky="nsew")

        self.min_label = Label(self, text=self.forecast.min_temp)
        self.min_label.configure(bg=background_color, fg=text_color, font=(font_type, actual_extrema_size))
        self.min_label.grid(row=4, column=0, sticky="nsew")

        max_text_label = Label(self, text="max")
        max_text_label.configure(bg=background_color, fg=text_color, font=(font_type, actual_extrema_size))
        max_text_label.grid(row=3, column=1, sticky="nsew")

        self.max_label = Label(self, text=self.forecast.min_temp)
        self.max_label.configure(bg=background_color, fg=text_color, font=(font_type, actual_extrema_size))
        self.max_label.grid(row=4, column=1, sticky="nsew")

        self.update_forecast()

    def update_forecast(self):
        self.forecast = get_forecast(day=self.day)

        min_text = str(self.forecast.min_temp)
        if min_text != default_return_error:
            min_text += "°C"
        max_text = str(self.forecast.max_temp)
        if max_text != default_return_error:
            max_text += "°C"

        self.min_label.configure(text=min_text)
        self.max_label.configure(text=max_text)

        self.forecast_image = get_weather_image(image_name=self.forecast.icon_name)

        self.image_label.configure(image=self.forecast_image)
        self.image_label.image = self.forecast_image

        self.after(forecast_update, self.update_forecast)
