text = input("Enter a sentence: ")

words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    print(word, ":", count)