# Write a program which accept number from user and display its table.


# Using for loop

n = int(input('Enter a number: '))
for i in range(1, 11):
    print(f' {n} * {i} = {n*i}')


# Using while loop

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1


# Using list comprehension

n = int(input("Enter a number: "))
table = [n * i for i in range(1, 11)]
print(table)


# Using function

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))
