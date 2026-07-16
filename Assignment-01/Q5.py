# Accept one number from user and print that number of * on screen

# Using string
num = int(input("Enter Number: "))
print("*"*num)

# Using for loop
num = int(input("Enter a number: "))
for i in range(num):
    print("*", end="")

# Using while loop
num = int(input("Enter a number: "))
i = 0
while i < num:
    print("*", end="")
    i += 1

# Using join
num = int(input("Enter a number: "))
print("".join(["*"] * num))