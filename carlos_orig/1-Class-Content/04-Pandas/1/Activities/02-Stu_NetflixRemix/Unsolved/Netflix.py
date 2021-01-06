
# coding: utf-8
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set variable to check if we found the video
found = False

# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")
print(csvpath)

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        movie = row[0]
        rating = row[1]
        score = row[5]
        if movie == video:
            print(f"The {movie} is rated {rating} with a score of {score}")

            # Set variable to confirm we have found the video
            found = True

    # If the video is never found, alert the user
    if not found:
        print("We don't seem to have what you are looking for!")
