# Write a program which accept distance in kilometre and convert it into meter.
# (1 kilometre = 1000 Meter)


# Using variable

kilometre = float(input("Enter distance in kilometre: "))
meter = kilometre * 1000
print("Distance in meter =", meter)


# Using function

def convert_to_meter(kilometre):
    return kilometre * 1000


km = float(input("Enter distance in kilometre: "))
print("Distance in meter =", convert_to_meter(km))
