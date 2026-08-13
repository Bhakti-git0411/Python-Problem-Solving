# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 4, iCol = 4
# Output: 1 2 3 4
#         2 3 4 5
#         3 4 5 6
#         4 5 6 7


n = int(input('Enter a row: '))
m = int(input('Enter a col: '))

for i in range(n):
    for j in range(m):
        print(i + j + 1, end=" ")
    print()
     