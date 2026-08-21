import sys
import csv
from tabulate import tabulate

table = []

if len(sys.argv) > 2 or len(sys.argv) == 1:
        sys.exit(1)

if sys.argv[1].endswith(".csv") == False:
    sys.exit(1)

with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    for row in reader:
        table.append(row)

print(tabulate(table, headers="firstrow", tablefmt="grid"))
