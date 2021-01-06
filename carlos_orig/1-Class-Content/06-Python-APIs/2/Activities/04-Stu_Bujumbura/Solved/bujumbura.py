# Dependencies
import requests as req

# Save config information.
api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
url = "http://api.openweathermap.org/data/2.5/weather?"
city = "Bujumbura"
units = "metric"

# Build query URL and request your results in Celsius
query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

# Get weather data
weather_response = req.get(query_url)
weather_json = weather_response.json()

# Get temperature from JSON response
temperature = weather_json["main"]["temp"]

# Report temperature
print("The temperature in Bujumbura is " + str(temperature) + ".")
