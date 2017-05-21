import requests


freegeoip = "http://freegeoip.net/json"
city = ""
country = ""

def get_city_country():
    geo_r = requests.get(freegeoip)
    geo_json = geo_r.json()

    city = geo_json["city"]
    country = geo_json["country_name"]

    return city, country

def get_lat_long():
    geo_r = requests.get(freegeoip)
    geo_json = geo_r.json()

    latitude = geo_json["latitude"]
    longitude = geo_json["longitude"]

    return latitude, longitude
