# -*- coding: UTF-8 -*-
"""Dictionary Operations.

* key/value pairs
* init methods {}, dict(zip()), fromkeys()
* accessing values, default values
* keys(), values(), items()
* iterating/changing values
* copy and update
* argument unpacking **
* string format
* csv.DictReader()
"""
import csv

# Empty
d = {}

# Key/Value Pairs
employee = {"first_name": "margaret", "last_name": "Hamilton"}
print(employee["first_name"])
print(employee["last_name"])

# Initialization
employee1 = {"first_name": "Robert", "last_name": "Goddard"}

employee2 = dict(first_name="Margaret", last_name="Hamilton")

keys = ["first_name", "last_name"]
values = ["John", "Glenn"]
employee3 = dict(zip(keys, values))

employee4 = {}.fromkeys(keys)
employee4["first_name"] = "Neil"
employee4["last_name"] = "Armstrong"

# Accessing Single Value
print(employee["first_name"])
employee.get("first_name")
# print(employee["firstname"])  # Broken
print(employee.get("firstname", "Key Not Found"))

# Changing a Value
employee["first_name"] = "M"
employee["first_name"] = "Margaret"

# All Keys
employee.keys()

# All Values
employee.values()

# Iterating over keys
for key in employee:
    print(key)

# Iterating over values
for value in employee.values():
    print(values)

# Iterating over keys and values
for key, value in employee.items():
    print("Key: {}".format(key))
    print("Value: {}".format(value))

# Copy
employee_copy = employee.copy()

# Update/Merge
title = {"title": "Computer Scientist"}
employee.update(title)

# Delete
del employee["title"]

# Updating/Merging Python 3.5+
employee = {**employee, **title}

# String Format
print("First Name: {first_name}, Last Name: {last_name}".format(**employee))

# Writing Dictionaries to CSV
with open("employees.csv", "w") as csvfile:
    fieldnames = ["last_name", "first_name"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(employee1)
    writer.writerow(employee2)
    writer.writerow(employee3)
    writer.writerow(employee4)

# Reading CSV to Dictionary
with open("employees.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print("{first_name}, {last_name}".format(**row))
