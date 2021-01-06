# Dependencies
import tweepy
import time
import os


# Twitter API Keys
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")


# Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    
# Quotes to Tweet
quote_list = ["Quote 1",
              "Quote 2",
              "Quote 3"]


# Create function for tweeting
def quote_it_up(quote):

    # Tweet the next quote
    api.update_status(quote)

    # Print success message
    print("Tweeted successfully, sir!")


# Create a loop that tweets one quote per minute until
# all of the quotes have been tweeted
for quote in quote_list:
    quote_it_up(quote)
    time.sleep(60)
