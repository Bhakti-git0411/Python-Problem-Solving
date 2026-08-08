# Write a program which accept number from user and return difference between summation of even digits and summation of odd digits


# Using while loop

num = int(input("Enter number: "))
even_sum = 0
odd_sum = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even_sum = even_sum + digit
    else:
        odd_sum = odd_sum + digit
    num = num // 10
difference = even_sum - odd_sum
print("Difference:", difference)
