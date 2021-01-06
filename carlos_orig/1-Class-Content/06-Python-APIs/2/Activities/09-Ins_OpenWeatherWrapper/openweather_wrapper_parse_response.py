# Dependencies
import openweathermapy.core as ow

# Create settings dictionary with information we're interested in
api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
settings = {"units": "metric", "appid": api_key}

# OpenWatherMapy makes it easy to parse the response
current_weather_paris = ow.get_current("Paris", **settings)
summary = ["name", "main.temp"]

data = current_weather_paris(*summary)
print("The current weather summary for Paris is: " + str(data))
