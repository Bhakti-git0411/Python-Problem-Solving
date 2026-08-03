# Write a program which accept N from user and print all odd numbers up to N


# Using for loop

n = int(input('Enter a num: '))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)


# Using while loop

n = int(input("Enter a number: "))
i = 1
while i <= n:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1


# Using list comprehension

n = int(input("Enter a number: "))
odd_numbers = [i for i in range(1, n + 1) if i % 2 != 0]
print(odd_numbers)


# Using range

n = int(input("Enter a number: "))
for i in range(1, n + 1, 2):  # start=1, step=2
    print(i, end=" ")
