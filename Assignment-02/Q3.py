# Accept number from user and check whether number is even or odd

# Using if-else
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Using conditional expression
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# Using list indexing
num = int(input("Enter a number: "))
print(["Even", "Odd"][num % 2])
