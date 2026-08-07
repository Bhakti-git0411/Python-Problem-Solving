# Write a program which accepts number from user and display its digits in reverse order.


# Using while loop

num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reverse:", reverse)


# Using for loop

num = input("Enter a number: ")
reverse = ""
for digit in num:
    reverse = digit + reverse
print("Reverse:", reverse)


# Using list and reverse method

num = input("Enter a number: ")
digits = list(num)
digits.reverse()
print("Reverse:", ''.join(digits))
