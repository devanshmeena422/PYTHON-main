def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])

# Example
print(reverse_words("Python is fun"))