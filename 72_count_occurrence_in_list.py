numbers = [1,2,3,2,4,2,5]

target = 2
count = 0

for num in numbers:
    if num == target:
        count += 1

print("Occurrences:", count)