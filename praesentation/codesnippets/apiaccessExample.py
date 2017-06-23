import pyowm
def get_weather():
    position = get_lat_long()
    w_api = pyowm.OWM(API_KEY)
    curr_w = w_api.weather_at_coords(lat=pos[0], lon=pos[1]).get_weather()
    return curr_w
