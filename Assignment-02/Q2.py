# Accept two numbers from user and display first number in second number of times

# Using for loop
a = int(input("Enter a number1: "))
b = int(input("Enter a number2: "))
for i in range(b):
    print(a, end=" ")

# Using while loop
a = int(input("Enter a number1: "))
b = int(input("Enter a number2: "))
i = 0
while i < b:
    print(a, end=" ")
    i += 1




