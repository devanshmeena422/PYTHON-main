import csv

total = 0

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += int(row["value"])

print("Total:", total)