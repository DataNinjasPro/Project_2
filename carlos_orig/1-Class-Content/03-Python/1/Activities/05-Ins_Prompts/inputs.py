
# Collects the user's input for the prompt "What is your name?"
name = input("What is your name? ")

# Collects the user's input for the prompt "How old are you?"
# and converts the string to an integer
age = int(input("How old are you? "))

# Collects the user's input for the prompt "Is this statement true?"
# and converts it to a boolean
is_true = bool(input("Is this statement true? "))

# Creates three print statements that to respond with the output
print(f"My name is {name}")
print(f"I am {age} years old.")
print(f"The statement was {is_true}")

