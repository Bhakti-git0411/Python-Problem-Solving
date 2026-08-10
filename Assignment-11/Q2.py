# Accept number from user and display below pattern
# Input: 5
# Output: 5 # 4 # 3 # 2 # 1 #


n = int(input('Enter a number: '))
for i in range(n, 0, -1):
    print(i, "#", end=" ")
