# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 5, iCol = 5
# Output: a b c d e
#         1 2 3 4 5
#         a b c d e
#         1 2 3 4 5
#         a b c d e


n = int(input('Enter a row: '))
m = int(input('Enter a col: '))

alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            print(alpha[j], end=' ')
        else:
            print(j + 1, end=' ')
    print()
