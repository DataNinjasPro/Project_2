# Dependencies
import openweathermapy.core as ow

# Create settings dictionary with information we're interested in
api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
settings = {"units": "metric", "appid": api_key}

# Get current weather
current_weather_paris = ow.get_current("Paris", **settings)
print("Current weather object for Paris: " + str(current_weather_paris))
