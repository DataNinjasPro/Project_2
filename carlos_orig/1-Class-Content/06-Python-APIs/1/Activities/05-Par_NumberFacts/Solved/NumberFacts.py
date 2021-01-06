# Dependencies
import requests as req
import json

# Base URL for GET requests to retrieve number/date facts
url = "http://numbersapi.com/"

# Ask the user what kind of data they would like to search for
kind_of_search = input("What type of data would you like to search for? [Trivia, Math, Date, or Year] ")

# If the kind of search is "date" take in two numbers
if(kind_of_search.lower() == "date"):

  # Collect the month to search for
  month = input("What month would you like to search for? ")
  # Collect the day to search for
  day = input("What day would you like to search for? ")

  # Make an API call to the "date" API and convert response object to JSON
  response = req.get(url + month + "/" + day + "/" +  kind_of_search.lower()+ "?json").json()
  # Print the fact stored within the response
  print(response["text"])

# If the kind of search is anything but "date" then take one number
else:

  # Collect the number to search for
  number = input("What number would you like to search for? ")

  # Make an API call to the API and convert response object to JSON
  response = req.get(url + number + "/" +  kind_of_search.lower()+ "?json").json()
  # Print the fact stored within the response
  print(response["text"])