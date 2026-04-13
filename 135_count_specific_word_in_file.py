word = input("Enter word to search: ")

count = 0

with open("data.txt", "r") as file:
    for line in file:
        count += line.lower().split().count(word.lower())

print("Count:", count)