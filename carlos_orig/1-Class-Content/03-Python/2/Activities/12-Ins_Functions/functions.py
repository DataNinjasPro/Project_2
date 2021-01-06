# Define the function and tell it to print "Hello!" when called
def print_hello():
    print("Hello!")
# Call the function within the application to ensure the code is run
print_hello()


# Functions that take in and use parameters can also be defined
def print_name(name):
    print(f"Hello {name}!")
# When calling a function with a parameter, a parameter must be passed into the function
print_name("Bob Smith")


# The prime use case for functions is in being able to run the same code for different values
first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_list = [11, 12, 13, 14, 15]

def display_information(simpleList):
    print("The values within the list are...")
    for value in simpleList:
        print(value)
    print(f"The length of this list is... {len(simpleList)}")

display_information(first_list)
display_information(second_list)
