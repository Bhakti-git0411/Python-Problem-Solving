# Write a Program which accept number from user and count frequency of such a digit which are less than 6.


# Using while loop

num = int(input("Enter a number: "))
count = 0
while num > 0:
    digit = num % 10
    if digit < 6:
        count += 1
    num = num // 10
print("Frequency:", count)


# Using for loop

num = input("Enter a number: ")
count = 0
for digit in num:
    if int(digit) < 6:
        count += 1
print("Frequency:", count)

