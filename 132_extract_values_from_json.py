import json

data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

names = []

for item in data:
    names.append(item["name"])

print(names)