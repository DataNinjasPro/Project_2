import glob
for file in glob.glob(".csv"):
    print(file)

from pathlib import Path
p = Path(".")
list(p.glob("*.py"))

import os
filepaths = []
for file in os.listdir("."):
    if file.endswith(".csv"):
        filepaths.append(file)
print(filepaths)
