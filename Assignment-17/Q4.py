# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 6  , iCol = 6
# Output: * * * * * *
#         * # # # * *
#         * # # * $ *
#         * # * $ $ *
#         * * $ $ $ *
#         * * * * * *


iRow = int(input("Enter number of rows: "))
iCol = int(input("Enter number of columns: "))

for i in range(iRow):
    for j in range(iCol):
        if i == 0 or i == iRow - 1:
            print("*", end=" ")
        elif j == 0 or j == iCol - 1:
            print("*", end=" ")
        elif i + j < iCol:
            print("#", end=" ")
        else:
            print("$", end=" ")
    print()