# Accept number from user and display below pattern
# Input: 4
# Output: # 1 * # 2 * # 3 * # 4 * 

n = int(input('Enter a number: '))
for i in range(1, n + 1):
    print('#', i, '*', end=' ')