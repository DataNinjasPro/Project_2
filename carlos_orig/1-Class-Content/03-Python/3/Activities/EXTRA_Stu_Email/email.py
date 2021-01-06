# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create a list of email addresses
using employee data from a csv file.

Example:
    $ python email.py

    Output: ['Tina@example.com', 'Erica@example.com']

"""
import os
import csv

# Establish the root path and resource path
filepath = os.path.join("Resources", "employees.csv")

# Read data into dictionary and create a list of emails by combining the
# `first_name` field and `@example.com`. The new email address will look
# like: `Tina@example.com`
new_emails = []
with open(file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        new_emails.append(f"{first_name}@example.com")

        # BONUS
        for key, value in row.items():
            print(f"{key}: {value}")

print(new_emails)
