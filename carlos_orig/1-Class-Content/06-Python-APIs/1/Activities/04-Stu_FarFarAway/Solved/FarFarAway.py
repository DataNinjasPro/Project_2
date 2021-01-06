# Dependencies
import requests as req
import json

# URL for GET requests to retrieve Star Wars character data
url = "https://swapi.co/api/people/"

# Storing the JSON response within a variable
response = req.get(url + '4').json()

# Collecting the name of the character collected
character_name = response["name"]

# Counting how many films the character was in
film_number = len(response["films"])

# Figure out what their first starship was
first_ship_url = response["starships"][0]
ship_response = req.get(first_ship_url).json()
first_ship = ship_response["name"]

# Print character name and how many films they were in
print(character_name + " was in " + str(film_number) + " films")
# Print what their first ship was
print("Their first ship: " + first_ship)