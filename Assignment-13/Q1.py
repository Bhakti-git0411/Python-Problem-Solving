# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 4, iCol = 4
# Output: A B C D
#         A B C D
#         A B C D
#         A B C D

n = int(input('Enter a row: '))
m = int(input('Enter a col: '))
for i in range(n):
    for j in range(m):
        print((chr(65+j)), end=' ')
    print()