# Write a program which accept number from user and print that number of $ & * on screen


n = int(input('Enter a number: '))
print("$" * n)
print("*" * n)


# Using for loop

n = int(input("Enter a number: "))
for i in range(n):
    print("$", end="")
print()
for i in range(n):
    print("*", end="")


# Using while loop

n = int(input("Enter a number: "))
i = 0
while i < n:
    print("$", end="")
    i += 1
print()
i = 0
while i < n:
    print("*", end="")
    i += 1
