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


# Target Term
target_term = "@DaDataBootcamp"


# Create a function that checks for tweets sent to the account,
# parses for hashtags, then responds with the weather.
def WeatherTweet():

    # Create a variable for storing the requested hashtag
    hashtag = ""

    # Search for most recent tweet directed to the account
    public_tweets = api.search(target_term, count=1, result_type="recent")

    # Early Return Pattern
    if not public_tweets["statuses"]:
        return

    # Extract hashtag from tweet directed to the account
    for tweet in public_tweets["statuses"]:

        # Print tweet in JSON
        print(
            json.dumps(
                tweet,
                sort_keys=True,
                indent=4))

        # Print tweet text
        print(tweet["text"])

        # Loop through all hashtags and print each one included
        for hashtag in tweet["entities"]["hashtags"]:

            # Store the hashtag
            hashtag = hashtag["text"]

            # Print the hashtag for display
            print(hashtag)

            # Utilize the hashtag to construct a Query URL for the OpenWeatherMap

            url = "http://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": hashtag,
                "units": "imperial",
                "appid": api_key
            }

            # Perform the API call to get the weather
            weather_response = requests.get(url, params=params)
            weather_json = weather_response.json()
            print(weather_json)

            # Tweet the weather
            api.update_status(
                "{} weather as of {}: {} F".format(
                    hashtag,
                    datetime.datetime.now().strftime("%I:%M %p"),
                    weather_json["main"]["temp"]))

            # Print success message
            print("Tweeted successfully, sir!")


# Set timer to run every 1 minute for 5 minutes
t_end = time.time() + 60 * 5
while time.time() < t_end:
    WeatherTweet()
    time.sleep(60)
