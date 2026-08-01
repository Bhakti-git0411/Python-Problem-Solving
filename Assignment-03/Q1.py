# Write a program which accept one number from user and print that number of even numbers on screen

# Using for loop
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i * 2, end=" ")

# Using while loop
n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i * 2, end=" ")
    i += 1

# Using range
n = int(input("Enter a number: "))
for i in range(2, 2 * n + 1, 2):
    print(i, end=" ")

# Using list comprehension
n = int(input("Enter a number: "))
print([i * 2 for i in range(1, n + 1)])
