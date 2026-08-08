# Write a program which accept number from user and return the count of even digits


# Using while loop

num = int(input("Enter number: "))
count = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        count += 1
    num = num // 10
print("Count of even digits:", count)