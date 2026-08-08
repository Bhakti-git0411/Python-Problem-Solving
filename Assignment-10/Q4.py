# Write a program which accept number from user and return multiplication of all digits


# Using while loop

num = int(input("Enter number: "))
mult = 1
while num > 0:
    digit = num % 10
    mult = mult * digit
    num = num // 10
print("Multiplication of all digits:", mult)