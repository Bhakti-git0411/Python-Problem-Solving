# Accept number from user and display below pattern
# Input: 5
# Output: A B C D E


n = int(input('Enter a num: '))
for i in range(n):
    print((chr(65+i) + ' '), end=' ')