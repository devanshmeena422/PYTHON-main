numbers = [12, 7, 25, 3, 18]

min_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num

print("Minimum number:", min_num)