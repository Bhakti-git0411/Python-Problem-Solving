# Write a program which accept number from user and display its table in reverse order


# Using for loop

n = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(n * i)


# Using while loop

n = int(input("Enter a number: "))
i = 10
while i >= 1:
    print(f"{n} x {i} = {n*i}")
    i -= 1


# Using list comprehension

n = int(input("Enter a number: "))
table = [f"{n} x {i} = {n*i}" for i in range(10, 0, -1)]
for row in table:
    print(row)


# Using function

def reverse_table(n):
    for i in range(10, 0, -1):
        print(f"{n} x {i} = {n * i}")


num = int(input("Enter a number: "))
reverse_table(num)