# Accept one number from user 
# If number is less than 10 then print "Hello" otherwise print "Demo"

# Using if-else
num = int(input("Enter a number: "))
if num < 10:
    print("Hello")
else:
    print("Demo")

# Using conditional expression
num = int(input("Enter a number: "))
print("Hello" if num < 10 else "Demo")
