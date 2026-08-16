# Accept number of rows and number of columns from user and display below pattern 
# Input: iRow = 4 , iCol = 4 
# Output: 1 2 3 4 
#           2 3 4 
#             3 4 
#               4


iRow = int(input("Enter number of rows: "))
iCol = int(input("Enter number of columns: "))

for i in range(iRow):
    print("  " * i, end="")

    for j in range(i, iCol):
        print(j + 1, end=" ")

    print()