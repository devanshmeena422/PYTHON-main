numbers = [5, 12, 7, 25, 9]

max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("Maximum number:", max_num)