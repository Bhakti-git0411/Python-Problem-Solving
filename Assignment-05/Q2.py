# Write a program which accept number from user and print numbers till that number


# Using for loop

n = int(input('Enter a num: '))
for i in range(0, n + 1):
    print(i, end=" ")


# Using while loop

n = int(input('Enter a num: '))
i = 0
while i <= n:
    print(i, end=" ")
    i += 1


# Using list comprehension

n = int(input("Enter a number: "))
print([i for i in range(0, n + 1)])


# Using list comprehension and join

n = int(input("Enter a number: "))
print(" ".join(str(i) for i in range(0, n + 1)))
