# Dependencies
import tweepy
import requests
import time
import datetime
import os


# Twitter API Keys
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

# Weather API
api_key = os.getenv("api_key")

# Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that gets the weather in London and Tweets it
def WeatherTweet():
    """Tweet the weather."""

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "London",
        "units": "imperial",
        "appid": api_key
    }

    # Perform the API call to get the weather
    weather_response = requests.get(url)
    weather_json = weather_response.json()
    print(weather_json)

    # Tweet the weather
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    weather = weather_json["main"]["temp"]
    api.update_status(f"London Weather as of {current_time}: {weather} F")

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every 1 hour for 24 hours
t_end = time.time() + 3600 * 24
while(time.time() < t_end):
    WeatherTweet()
    time.sleep(3600)
