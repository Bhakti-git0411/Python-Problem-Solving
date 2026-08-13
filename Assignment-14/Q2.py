# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 4, iCol = 5
# Output: 2 4 6 8 10
#         1 3 5 7 9
#         2 4 6 8 10
#         1 3 5 7 9


n = int(input('Enter a row: '))
m = int(input('Enter a col: '))

for i in range(n):
    if i % 2 == 0:
        num = 2
    else:
        num = 1
    for j in range(m):
        print(num, end=' ')
        num = num + 2
    print()
