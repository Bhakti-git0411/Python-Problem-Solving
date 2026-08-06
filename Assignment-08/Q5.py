# Write a program which accept area in square feet and convert it into square meter.
# (1 square feet = 0.0929 Square meter)


# Using variable

square_feet = float(input("Enter area in square feet: "))
square_meter = square_feet * 0.0929
print("Area in square meter =", square_meter)


# Using function

def convert_to_square_meter(square_feet):
    return square_feet * 0.0929


area = float(input("Enter area in square feet: "))
print("Area in square meter =", convert_to_square_meter(area))
