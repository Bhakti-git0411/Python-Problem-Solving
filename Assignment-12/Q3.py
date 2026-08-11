# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 3, iCol = 5
# Output: 5 4 3 2 1
#         5 4 3 2 1
#         5 4 3 2 1


iRow = int(input('Enter a row : '))
iCol = int(input('Enter a col : '))
for i in range(iRow):
    for j in range(iCol):
        print(iCol-j, end=' ')
    print()