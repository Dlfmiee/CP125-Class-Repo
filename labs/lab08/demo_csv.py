import csv

# Read CSV file
f = open("labs/lab08/data/students.csv", "r", newline="")
reader = csv.reader(f)

for row in reader:
    print(row)

f.close()