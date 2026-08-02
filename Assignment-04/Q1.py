# Write a program which accept number from user and display its multiplication of factors


# Using for loop

n = int(input("Enter a number: "))
mul = 1
for i in range(1, n+1):
    if n % i == 0:
        mul *= i
print("Multiplication of factors is: ", mul)


# Using while loop

n = int(input("Enter a number: "))
i, mul = 1, 1
while i <= n:
    if n % i == 0:
        mul *= i
    i += 1
print("Multiplication of factors:", mul)


# Using list comprehension

import math
n = int(input("Enter a number: "))
factors = [i for i in range(1, n + 1) if n % i == 0]
print("Multiplication of factors:", math.prod(factors))
