# Write a program to find factorial of given number


# Using for loop

n = int(input('Enter a number: '))
fact = 1
for i in range(1, n + 1):
    fact = fact * i

print('Factorial is:', fact)


# Using while loop

n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:", fact)
