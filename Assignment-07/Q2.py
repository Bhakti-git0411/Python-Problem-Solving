# Accept amount in US Dollar and return its corresponding value in Indian Currency. Consider 1$ = 70 Rupees.


dollar = float(input("Enter amount in US Dollar: "))
rupees = dollar * 70
print("Indian Currency =", rupees)


# Using function

def convert(dollar):
    return dollar * 70


dollar = float(input("Enter amount in US Dollar: "))
print("Indian Currency =", convert(dollar))
