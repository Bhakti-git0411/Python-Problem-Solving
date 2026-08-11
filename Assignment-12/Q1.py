# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 4, iCol = 3
# Output: * * *
#         * * *
#         * * *
#         * * *


iRow = int(input('Enter a row : '))
iCol = int(input('Enter a col : '))
for i in range(iRow):
    for j in range(iCol):
        print('*', end=' ')
    print()