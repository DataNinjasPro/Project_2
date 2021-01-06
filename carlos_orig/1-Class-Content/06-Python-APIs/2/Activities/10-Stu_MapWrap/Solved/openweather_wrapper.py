# Dependencies
import csv
import matplotlib.pyplot as plt

import openweathermapy as ow
import pandas as pd

# Create a settings object with your API key and preferred units
api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
settings = {"units": "metric", "appid": api_key}

# Get data for each city in cities.csv
weather_data = []
with open("../Resources/cities.csv") as cities:
    cities = csv.reader(cities)
    cities = [city[0] for city in cities]
    weather_data = [ow.get_current(city, **settings) for city in cities]

# Create an "extracts" object to get the temperature, latitude,
# and longitude in each city
summary = ["main.temp", "coord.lat", "coord.lon"]

# Create a Pandas DataFrame with the results
data = [response(*summary) for response in weather_data]

column_names = ["Temperature", "Latitude", "Longitude"]
weather_data = pd.DataFrame(data, index=cities, columns=column_names)
