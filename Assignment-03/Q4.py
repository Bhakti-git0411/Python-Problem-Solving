# Accept one character from user and convert case of that character

# Using .islower() and .isupper()
ch = input("Enter a character: ")
if ch.islower():
    print(ch.upper())
elif ch.isupper():
    print(ch.lower())
else:
    print(ch)

# Using swapcase
ch = input("Enter a character: ")
print(ch.swapcase())
