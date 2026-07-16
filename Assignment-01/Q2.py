# Program to divide two numbers

# Using simple division
a = 25
b = 5
print("The Division is: ", a / b)

# Using user input
a = int(input("Enter Num1: "))
b = int(input("Enter Num2: "))
print("The Division is: ", a / b)

# Using floor division
a = 25
b = 5
print("The Floor Division is: ", a // b)

# Using if-else
a = float(input('A: '))
b = float(input('B: '))
if b != 0:
    print('The Division is: ', a / b)
else:
    print('Not divisible by 0')

# Using error handling
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
