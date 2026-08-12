# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 3, iCol = 4
# Output: 1 2  3  4
#         5 6  7  8
#         9 10 11 12

n = int(input('Enter a row: '))
m = int(input('Enter a col: '))
num = 1
for i in range(n):
    for j in range(m):
        print(num, end=' ')
        num = num + 1
    print()
