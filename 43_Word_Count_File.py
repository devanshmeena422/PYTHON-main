def word_count(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

# Input
filename = input("Enter file name: ")

try:
    print("Total words:", word_count(filename))
except FileNotFoundError:
    print("File not found")