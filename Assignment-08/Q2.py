# Write a program which accept width & height of rectangle from user and calculate its area.
# (Area = Width * Height)


# Using variable

width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))
area = width * height
print("Area of the rectangle =", area)


# Using function

def calculate_area(width, height):
    return width * height


w = float(input("Enter width: "))
h = float(input("Enter height: "))
print("Area =", calculate_area(w, h))
