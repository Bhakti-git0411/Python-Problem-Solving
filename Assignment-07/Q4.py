# Write a program to find odd factorial of a given number.


# Using for loop

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1, 2):
    fact = fact * i
print("Odd Factorial =", fact)


# Using while loop

num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 2
print("Odd Factorial =", fact)


# Using list

num = int(input("Enter a number: "))
odd_numbers = []
for i in range(1, num + 1, 2):
    odd_numbers.append(i)
fact = 1
for value in odd_numbers:
    fact = fact * value
print("Odd Factorial =", fact)


# Using function

def odd_factorial(num):
    fact = 1
    for i in range(1, num + 1, 2):
        fact = fact * i
    return fact


num = int(input("Enter a number: "))
print("Odd Factorial =", odd_factorial(num))
