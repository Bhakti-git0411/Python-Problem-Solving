# Write a Program which accept number from user and return the count of digits in between 3 and 7


# Using while loop

num = int(input("Enter number: "))
count = 0
while num > 0:
    digit = num % 10
    if digit > 3 and digit < 7:
        count += 1
    num = num // 10
print("Count of digits between 3 and 7:", count)