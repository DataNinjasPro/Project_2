import random
from names import part1, part2, part3, part4

def superhero(initials):
    """Supply your initials and get back a superhero name!."""

    first_initial, middle_initial, last_initial = initials
    first = part1[first_initial]
    second = part2[last_initial]
    third = random.choice(part3)
    fourth = part4[middle_initial]
    return f"{first} {second} {third} {fourth}"

initials = input("What are your initials? ")

print("Your SuperHero name is:")
print(superhero(initials))
