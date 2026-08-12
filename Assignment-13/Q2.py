# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 4, iCol = 4
# Output: A B C D
#         a b c d
#         A B C D
#         a b c d

n = int(input('Enter a row: '))
m = int(input('Enter a col: '))
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            print(alpha[j].upper(), end=' ')
        else:
            print(alpha[j].lower(), end=' ')
    print()
