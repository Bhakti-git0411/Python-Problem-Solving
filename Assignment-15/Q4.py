# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 5  , iCol = 5
# Output: * * * * *
#         * @ @ @ *
#         * @ @ @ *
#         * @ @ @ *
#         * * * * *


iRow = int(input("Enter number of rows: "))
iCol = int(input("Enter number of columns: "))

for i in range(1, iRow + 1):
    for j in range(1, iCol + 1):
        if i == 1 or i == iRow or j == 1 or j == iCol:
            print("*", end=" ")
        else:
            print("@", end=" ")
    print()