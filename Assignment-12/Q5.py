# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 3, iCol = 4
# Output: 1 1 1 1
#         2 2 2 2
#         3 3 3 3


n = int(input('Enter a row: '))
m = int(input('Enter a col: '))
for i in range(1,n+1):
    for j in range(m):
        print(i , end=' ')
    print()