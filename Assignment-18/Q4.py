# Accept N numbers from the user and display all such elements which are divisible by 3 and 5.
# Input:  N:  6
#         Elements: 85 66 3 15 93 88
# Output: 15


n = int(input("Enter N: "))

print("Enter elements:")

for i in range(n):
    num = int(input())

    if num % 3 == 0 and num % 5 == 0:
        print(num, end=" ")