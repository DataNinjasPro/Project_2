import os


filepath = os.path.join('.', 'myfile.txt')

total = 0

with open(filepath, 'r') as fh:
    # Iterate and Read
    for line in fh:
        total = total + int(line)

print(f"The total was: {total}")
