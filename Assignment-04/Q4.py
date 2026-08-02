# Write a program which accept number from user and return summation of all its non factors

# Using for loop

def sum_non_factors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i != 0:
            total += i
    return total
n = int(input('Enter a num: '))
print('The summation is: ', sum_non_factors(n))


# Using while loop

def sum_non_factors(n):
    total = 0
    i = 1
    while i <= n:
        if n % i != 0:   # check non-factor
            total += i
        i += 1
    return total
num = int(input("Enter a number: "))
print("Summation of non-factors:", sum_non_factors(num))


# Using list comprehension

def sum_non_factors(n):
    return sum([i for i in range(1, n + 1) if n % i != 0])
num = int(input("Enter a number: "))
print("Summation of non-factors:", sum_non_factors(num))
