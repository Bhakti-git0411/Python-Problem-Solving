# Write a program which accept number from user and if number is less than 50 then print small,
# if it is greater than 50 and less than 100 then print medium,
# if it is greater than 100 then print large


# Using elif 50 < n< 100

n = int(input("Enter a number: "))
if n < 50:
    print("small")
elif 50 < n < 100:   # cleaner way
    print("medium")
else:
    print("large")


# Using nested if else

n = int(input("Enter a number: "))
if n < 50:
    print("small")
else:
    if n < 100:
        print("medium")
    else:
        print("large")
