# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 3, iCol = 5
# Output: A A A A A
#         B B B B B
#         C C C C C


n = int(input('Enter a row: '))
m = int(input('Enter a col: '))
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(n):
    for j in range(m):
        print(alpha[i], end=' ')
    print()