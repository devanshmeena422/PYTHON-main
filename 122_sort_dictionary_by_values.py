data = {
    "apple": 5,
    "banana": 2,
    "orange": 8,
    "grape": 3
}

sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

print("Sorted by values:", sorted_data)