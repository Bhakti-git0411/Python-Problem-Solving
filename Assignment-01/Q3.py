# Program to print 5 to 1 numbers on screen

# Using for loop
for i in range(5, 0, -1):
    print(i)

# Using while loop
i = 5
while i >= 1:
    print(i)
    i -= 1

# Using reversed()
for i in reversed(range(1, 6)):
    print(i)

# Using slicing
l = [1, 2, 3, 4, 5]
for i in l[::-1]:
    print(i)