# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 4  , iCol = 4
# Output: 1 2 3 4
#         1 * * 4
#         1 * * 4
#         1 2 3 4


iRow = int(input("Enter number of rows: "))
iCol = int(input("Enter number of columns: "))

for i in range(1, iRow + 1):
    for j in range(1, iCol + 1):
        if i == 1 or i == iRow:
            print(j, end=" ")
        elif j == 1:
            print(1, end=" ")
        elif j == iCol:
            print(iCol, end=" ")
        else:
            print("*", end=" ")
    print()