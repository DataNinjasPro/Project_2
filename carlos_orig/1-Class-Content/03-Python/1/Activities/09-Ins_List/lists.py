# Create a variable and set it as an List
my_list = ["Jacob", 25, "Ahmed", 80]
print(my_list)

# Adds an element onto the end of a List
my_list.append("Matt")
print(my_list)

# Select the third element in the list
print(my_list[3])

# Select the last element in the list
print(my_list[-1])

# Subset a list
print(my_list[1:3])

# Changes a specified element within an List at the given index
my_list[3] = 85
print(my_list)

# Returns the index of the first object with a matching value
print(my_list.index("Matt"))

# Returns the length of the List
print(len(my_list))

# Removes a specified object from an List
my_list.remove("Matt")
print(my_list)

# Removes the object at the index specified
my_list.pop(0)
my_list.pop(0)
print(my_list)

# Creates a tuple, a sequence of immutable Python objects that cannot be changed
myTuple = ('Python', 100, 'VBA', False)
print(myTuple)
