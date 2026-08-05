# Write a program which returns the difference between Even Factorial and Odd Factorial of a given number.


# Using for loop

num = int(input("Enter a number: "))
even_fact = 1
odd_fact = 1
for i in range(1, num + 1):
    if i % 2 == 0:
        even_fact = even_fact * i
    else:
        odd_fact = odd_fact * i
print("Difference =", even_fact - odd_fact)


# Using while loop

num = int(input("Enter a number: "))
even_fact = 1
odd_fact = 1
i = 1
while i <= num:
    if i % 2 == 0:
        even_fact = even_fact * i
    else:
        odd_fact = odd_fact * i
    i += 1
print("Difference =", even_fact - odd_fact)


# Using function

def even_factorial(num):
    fact = 1
    for i in range(2, num + 1, 2):
        fact *= i
    return fact


def odd_factorial(num):
    fact = 1
    for i in range(1, num + 1, 2):
        fact *= i
    return fact


num = int(input("Enter a number: "))
difference = even_factorial(num) - odd_factorial(num)
print("Difference =", difference)
