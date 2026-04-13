data = {"a": 20, "b": 60, "c": 45, "d": 80}

filtered = {}

for key, value in data.items():
    if value > 50:
        filtered[key] = value

print(filtered)