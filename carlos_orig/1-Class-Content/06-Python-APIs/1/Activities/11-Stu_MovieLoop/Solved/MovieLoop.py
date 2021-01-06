# Dependencies
import requests as req

url = "http://www.omdbapi.com/?apikey=40e9cece&t="

_movies = []
movies = ["Aliens", "Sing", "Moana"]

for movie in movies:
    _movie = req.get(url + movie).json()
    print("The director of " + movie + " is '" + _movie["Director"] + "'.")
