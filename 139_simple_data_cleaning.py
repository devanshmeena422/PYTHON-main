data = [10, None, 20, None, 30, 40]

cleaned = []

for item in data:
    if item is not None:
        cleaned.append(item)

print("Cleaned data:", cleaned)