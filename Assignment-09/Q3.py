# Write a program which accept number from user and count frequency of 2 in it.


# Using while loop

num = int(input("Enter a number: "))
count = 0
while num > 0:
    digit = num % 10
    if digit == 2:
        count += 1
    num = num // 10
print("Frequency of 2:", count)


# Using for loop

num = input("Enter a number: ")
count = 0
for digit in num:
    if digit == "2":
        count += 1
print("Frequency of 2:", count)


# Using count() method

num = input("Enter a number: ")
count = num.count("2")
print("Frequency of 2:", count)