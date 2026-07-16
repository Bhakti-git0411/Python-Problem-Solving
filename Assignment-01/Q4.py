# Accept one number and check whether it is divisible by 5 or not

# Using if-else
num = int(input("Enter Number: "))
if num % 5 == 0:
    print("The number is divisible by 5")
else:   
    print("The number is not divisible by 5")

# Using conditional expression
num = int(input("Enter a number: "))
print("Divisible by 5" if num % 5 == 0 else "Not divisible by 5")