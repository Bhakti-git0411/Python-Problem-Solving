# Accept single digit number from user and print it into word


n = int(input('Enter Digit: '))
if n == 0:
    print("zero")
elif n == 1:
    print('one')
elif n == 2:
    print('two')
elif n == 3:
    print('three')
elif n == 4:
    print('four')
elif n == 5:
    print('five')
elif n == 6:
    print('six')
elif n == 7:
    print('seven')
elif n == 8:
    print('eight')
elif n == 9:
    print('nine')
else:
    print('pls enter digit from 0 to 9 only')


# Using dictionary

digits = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
n = int(input("Enter Digit: "))
print(digits.get(n, "pls enter digit from 0 to 9 only"))
