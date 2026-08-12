# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 4, iCol = 5
# Output: 4 4 4 4 4 
#         3 3 3 3 3
#         2 2 2 2 2
#         1 1 1 1 1


n = int(input('Enter a row: '))
m = int(input('Enter a col: '))
for i in range(n, 0, -1):
    for j in range(m):
        print(i, end=' ')
    print()