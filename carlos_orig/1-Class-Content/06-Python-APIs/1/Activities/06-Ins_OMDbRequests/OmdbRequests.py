import requests
import json

# Note that the ?t= is a query param for the t-itle of the
# movie we want to search for.
url = "http://www.omdbapi.com/?t="
api_key = "&apikey=40e9cece"

# Performing a GET request similar to the one we executed
# earlier
response = requests.get(url + "Aliens" + api_key)

# Converting the response to JSON, and printing the result.
json = response.json()
print(json)

# Print a few keys from the response JSON.
print("Movie was directed by " + json["Director"])
print("Movie was released in " + json["Country"])
