# Write a program which accept temperature in Fahrenheit and convert it into celsius.
# (1 celsius =(Fahrenheit -32)*(5/9))


# Using variable

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * (5 / 9)
print("Temperature in Celsius =", celsius)


# Using function

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


f = float(input("Enter temperature in Fahrenheit: "))
print("Temperature in Celsius =", convert_to_celsius(f))
