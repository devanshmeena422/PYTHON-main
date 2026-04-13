numbers = [1, 2, 4, 6, 7]

n = 7

missing = []

for i in range(1, n + 1):
    if i not in numbers:
        missing.append(i)

print("Missing numbers:", missing)