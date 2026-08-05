# Write a program to find even factorial of a given number.


# Using for loop

num = int(input("Enter a number: "))
fact = 1
for i in range(2, num + 1, 2):
    fact = fact * i
print("Even Factorial =", fact)


# Using while loop

num = int(input("Enter a number: "))
fact = 1
i = 2
while i <= num:
    fact = fact * i
    i = i + 2
print("Even Factorial =", fact)


# Using function

def even_factorial(num):
    fact = 1
    for i in range(2, num + 1, 2):
        fact = fact * i
    return fact


num = int(input("Enter a number: "))
print("Even Factorial =", even_factorial(num))
