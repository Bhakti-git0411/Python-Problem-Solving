# Accept N numbers from the user and return frequency of even numbers
# Input:  N:  6
#         Elements: 85 66 3 80 93 88
# Output: 3


n = int(input("N: "))
elements = list(map(int, input("Elements: ").split()))

count = 0

for num in elements:
    if num % 2 == 0:
        count += 1

print(count)