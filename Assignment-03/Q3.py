# Write a program which accept one number from user and print even factors of that number

# Using for loop
n = int(input("Enter a number: "))
for i in range(1, n+1):
    if n % i == 0 and i % 2 == 0:
        print(i, end=" ")

# Using while loop
n = int(input("Enter a number: "))
i = 1
while i <= n:
    if n % i == 0 and i % 2 == 0:
        print(i, end=" ")
    i += 1

# Using list comprehension
n = int(input("Enter a number: "))
even_factors = [i for i in range(2, n + 1, 2) if n % i == 0]
print(even_factors)
