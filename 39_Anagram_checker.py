def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# Input
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if is_anagram(s1, s2):
    print("Anagram")
else:
    print("Not Anagram")