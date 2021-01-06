# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Play the game
if (user_choice == computer_choice):
    print(f"You both chose {user_choice}")
    print("A smashing tie!")
elif (user_choice == "r" and computer_choice == "s"):
    print(f"You chose {user_choice}. The computer chose {computer_choice}")
    print("Yay! You won.")
elif (user_choice == "p" and computer_choice == "r"):
    print(f"You chose {user_choice}. The computer chose {computer_choice}")
    print("Yay! You won.")
elif (user_choice == "s" and computer_choice == "p"):
    print(f"You chose {user_choice}. The computer chose {computer_choice}")
    print("Yay! You won.")
else:
    print(f"You chose {user_choice}. The computer chose {computer_choice}")
    print("Sorry. You lose.")
