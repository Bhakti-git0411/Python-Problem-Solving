# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 4, iCol = 3
# Output: 1 2 3
#         1 2 3
#         1 2 3
#         1 2 3


iRow = int(input('Enter a row : '))
iCol = int(input('Enter a col : '))
for i in range(iRow):
    for j in range(1, iCol + 1):
        print(j, end=' ')
    print()