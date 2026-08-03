# Write a program which accept N and print first 5 multiples of N


# Using for loop

n = int(input('Enter a num: '))
for i in range(1, 6):
    print(i*n, end=" ")


# Using while loop

n = int(input("Enter a number: "))
i = 1
while i <= 5:
    print(n * i, end=" ")
    i += 1


# Using list comprehension

n = int(input("Enter a number: "))
multiples = [n * i for i in range(1, 6)]
print(multiples)
