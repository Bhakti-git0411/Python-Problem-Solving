# Accept N numbers from the user and return difference between frequency of even numbers and odd numbers
# Input:  N:  7
#         Elements: 85 66 3 80 93 88 90
# Output: 1  (4-3)


n = int(input("N: "))
elements = list(map(int, input("Elements: ").split()))

even_count = 0
odd_count = 0

for num in elements:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count - odd_count)