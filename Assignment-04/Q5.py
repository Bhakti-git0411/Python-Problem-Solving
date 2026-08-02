# Write a program which accept number from user and return difference between summation of all its factors and non factors


# Using for loop

def diff_fact_nonfact(n):
    total = 0
    total_non = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
        else:
            total_non += i
    return total - total_non
n = int(input('Enter num: '))
print('The difference between summation is: ', diff_fact_nonfact(n))


# Using while loop

def diff_fact_nonfact(n):
    sum_fact = 0
    sum_nonfact = 0
    i = 1
    while i <= n:
        if n % i == 0:
            sum_fact += i
        else:
            sum_nonfact += i
        i += 1
    return sum_fact - sum_nonfact
num = int(input("Enter a number: "))
print("Difference:", diff_fact_nonfact(num))
