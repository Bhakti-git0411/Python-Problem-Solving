# Accept number from user and display below pattern
# Input: 8
# Output: 2 4 6 8 10 12 14 16

n = int(input('Enter a number: '))
for i in range(1, n+1):
    print(i*2, end=' ')
