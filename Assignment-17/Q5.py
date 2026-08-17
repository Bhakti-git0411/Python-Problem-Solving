# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 5  , iCol = 5
# Output: 1 2 3 4 5
#         1 2     5
#         1   3   5
#         1     4 5
#         1 2 3 4 5


iRow = int(input("Enter number of rows: "))
iCol = int(input("Enter number of columns: "))

for i in range(iRow):
    for j in range(iCol):
        if i == 0 or i == iRow - 1:
            print(j + 1, end=" ")
        elif j == 0 or j == iCol - 1:
            print(j + 1, end=" ")
        elif i == j:
            print(j + 1, end=" ")
        else:
            print(" ", end=" ")
    print()