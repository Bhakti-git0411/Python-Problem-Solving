# Accept number of rows and number of columns from user and display below pattern
# Input: iRow = 3, iCol = 4
# Output: * # * #
#         * # * #
#         * # * #


n = int(input('Enter a row: '))
m = int(input('Enter a col: '))
for i in range(n):
    for j in range(1, m+1):
        if j % 2 == 0:
            print('#', end=' ')
        else:
            print('*', end=' ')
    print()
