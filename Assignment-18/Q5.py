# Accept N numbers from the user and display all such elements which are multiples of 11
# Input:  N:  6
#         Elements: 85 66 3 55 93 88
# Output: 66 55 88


n = int(input("Enter N: "))

print("Enter elements:")

for i in range(n):
    num = int(input())

    if num % 11 == 0:
        print(num, end=" ")