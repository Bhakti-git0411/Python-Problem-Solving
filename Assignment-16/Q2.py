# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 4 , iCol = 4
# Output: * * * *
#         * * *
#         * *
#         *


iRow = int(input("Enter number of rows: "))
iCol = int(input("Enter number of columns: "))

for i in range(iRow, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
