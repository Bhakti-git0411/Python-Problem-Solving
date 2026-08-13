# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 4, iCol = 4
# Output: 1 2 3 4
#         5 6 7 8
#         9 1 2 3
#         4 5 6 7


n = int(input('Enter a row: '))
m = int(input('Enter a col: '))

num = 1

for i in range(n):
    for j in range(m):
        print(num, end=' ')
        num = num + 1
        if num > 9:
            num = 1
    print()
