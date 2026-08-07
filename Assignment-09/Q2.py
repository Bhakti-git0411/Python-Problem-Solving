# Write a program which accept number from user and check whether it contains 0 in it or not.


# Using while loop

num = int(input("Enter a number: "))
found = False
while num > 0:
    digit = num % 10

    if digit == 0:
        found = True
        break
    num = num // 10
if found:
    print("Number contains 0")
else:
    print("Number does not contain 0")


# Using for loop

num = input("Enter a number: ")
found = False
for digit in num:
    if digit == "0":
        found = True
        break
if found:
    print("Number contains 0")
else:
    print("Number does not contain 0")


# Using in operator

num = input("Enter a number: ")
if "0" in num:
    print("Number contains 0")
else:
    print("Number does not contain 0")