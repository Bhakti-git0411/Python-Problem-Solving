# Write a program which accept number from user and display its factors in decreasing

# for loop

n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    if n % i == 0:
        print(i, end=" ")
print("Factors in decreasing order:")


# while loop

n = int(input("Enter a number: "))
i = n
factors = []
while i >= 1:
    if n % i == 0:
        factors.append(i)
    i -= 1
print("Factors in decreasing order:")
print(factors)


# list comprehension

n = int(input("Enter a number: "))
print([i for i in range(n, 0, -1) if n % i == 0])
