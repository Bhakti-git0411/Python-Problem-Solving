# Write a program which accept radius of circle from user and calculate its area.
# Consider value of PI as 3.14.(Area = PI * Radius * Radius)


# Using variable

PI = 3.14
radius = float(input("Enter the radius of the circle: "))
area = PI * radius * radius
print("Area of the circle =", area)


# Using function

PI = 3.14
def calculate_area(radius):
    return PI * radius * radius


r = float(input("Enter radius: "))
print("Area =", calculate_area(r))
