# Write a program which accept number from user and display below pattern
# Input: 5
# *
# * *
# * * *
# * * * *
# * * * * *


# Using for loop

num = int(input("Enter a number: "))
for i in range(1, num + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# Using while loop

num = int(input("Enter a number: "))
i = 1
while i <= num:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1


# Using function

def pattern(num):
    for i in range(1, num + 1):
        for j in range(i):
            print("*", end=" ")
        print()


num = int(input("Enter a number: "))
pattern(num)
