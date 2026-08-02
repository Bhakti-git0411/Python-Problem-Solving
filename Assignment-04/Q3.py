# Write a program which accept number from user and display all its non factors

# Using for loop

n = int(input("Enter a number: "))
print('Non factors: ')
for i in range(1, n):
    if n % i != 0:
        print(i)


# Using while loop

n = int(input("Enter a number: "))
i = 1
while i <= n:
    if n % i != 0:
        print(i, end=" ")
    i += 1


# Using list comprehension

n = int(input("Enter a number: "))
non_factors = [i for i in range(1, n + 1) if n % i != 0]
print(non_factors)

