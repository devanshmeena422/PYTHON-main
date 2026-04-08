import csv

count = 0

with open("data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        count += 1

print("Total rows:", count)