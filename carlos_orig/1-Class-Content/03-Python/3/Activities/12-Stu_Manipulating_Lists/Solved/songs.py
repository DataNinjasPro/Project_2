# -*- coding: UTF-8 -*-
"""Favorite Songs

This module allows a user to enter their favorite songs, and how many
times they've listened to each. It then prints a list of songs
to the console, and reports whether one of the user's favorite songs
is Stairway to Heaven.

Example:

  $ python songs.py

"""

num_songs = input("How many favorite songs do you have? ")
num_songs = int(num_songs)

favorites = []
for num in range(1, num_songs + 1):
    favorite_song = input(f"What's your #{num + 1} favorite song? ")
    favorites.append(favorite_song)

favorites = set(favorites)

num_listens = []
for song in favorites:
    times_heard = input(f"How many times have you listened to {song}? ")
    times_heard = int(times_heard)
    num_listens.append(times_heard)

print("Here's a list of your favorite songs:")
for index, song in enumerate(favorites, 1):
    print(f"{index}. {song}")

# BONUS
most_frequent = max(num_listens)
least_frequent = min(num_listens)
total_listens = sum(num_listens)

output = (
    f"The most you've listened to a favorite song is {most_frequent} times.\n"
    f"The least you've listened to a favorite song is {least_frequent} times.\n"
    f"In total, you've listened to your songs {total_listens} times."
)

print(output)

stairway = "Stairway to Heaven" in favorites
print(f"It is {stairway} that one of your favorite songs is Stairway to Heaven.")
