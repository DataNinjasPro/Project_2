# -*- coding: UTF-8 -*-
"""Merge Records Script.

This module allows us to merge and output multiple csv files
into a single csv file.

Example:
    $ python merge_records.py

"""
import glob
import csv

# Iterate through the listdir results
filepaths = glob.glob("*.csv")

# Create a list to hold all csv data
all_csv_data = []

# Read each csv file and append the contents to the all_csv_data list
for file in filepaths:
    with open(file, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csvdata = list(csvreader)
        # @NOTE: We use index slicing to skip the header line from each file
        all_csv_data.extend(csvdata[1:])

# Write the merged data to a new file.
csvpath = "merged_records.csv"
with open(csvpath, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["First Name", "Last Name", "SSN"])
    csvwriter.writerows(all_csv_data)
