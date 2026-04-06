numbers = [10, 20, 30, 40, 50]

element = int(input("Enter number to remove: "))

if element in numbers:
    numbers.remove(element)

print("Updated list:", numbers)