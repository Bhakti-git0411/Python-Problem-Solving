# Accept N numbers from the user and return frquency of 11 from it.
# Input:  N:  6
#         Elements: 85 66 11 80 93 11 
# Output: 2


n = int(input("N: "))
elements = list(map(int, input("Elements: ").split()))

count = 0

for num in elements:
    if num == 11:
        count += 1

print(count)