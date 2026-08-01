# Accept one character from user and check whether that character is vowel or not

# Using if-else
ch = input("Enter a character: ")
if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Not Vowel")

# Using in with string
ch = input("Enter a character: ")
if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Not Vowel")

# Using set
ch = input("Enter a character: ")
vowels = {'a', 'e', 'i', 'o', 'u'}
print("Vowel" if ch.lower() in vowels else "Not Vowel")
