# Accept N numbers from the user and accept one another number as NO , return frequency of NO from it.
# Input:  N:  6
#         NO: 66
#         Elements: 85 66 11 80 93 66
# Output: 2


n = int(input("N: "))
no = int(input("NO: "))
elements = list(map(int, input("Elements: ").split()))

count = 0

for num in elements:
    if num == no:
        count += 1

print(count)