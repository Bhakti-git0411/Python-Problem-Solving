# Accept one number from user and print that number of # on screen.

# Using string
n = int(input('Enter a number:'))
print('#' * n)

# For loop
n = int(input('Enter a number:'))
for i in range(n):
    print('#', end='')

# While loop
n = int(input('Enter a number:'))
i = 0
while i < n:
    print('#', end='')
    i += 1
