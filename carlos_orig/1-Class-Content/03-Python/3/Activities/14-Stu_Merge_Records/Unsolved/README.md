# Manipulating CSV Files

In this activity, you will generate a Python script to read, write, and merge csv files.

## Instructions

* Import [os](https://docs.python.org/3/library/os.html) and [csv](https://docs.python.org/3/library/csv.html).

* Create a script to read all csv files in Resources directory, merge the data from all csv files, and write the merged data to the output directory.

  * Utilize `os.listdir`, `glob.glob`, or `pathlib` to find all csv files inside of the Resources directory.

  * Create an empty list named `all_csv_data` to hold all of the merged csv data.

  * Use csv.reader to read the data from each csv file and add the rows to `all_csv_data`.

    * Note: Make sure to strip off the header from each file and only include it once at the beginning of the merged data.

  * Open a new file in the output directory, called `merged_records.csv`, and use csv.write to output the all_csv_data as a single comma-delimited csv file.
