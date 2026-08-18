# Accept N numbers from the user and return difference between summation of even elements and summation of odd elements
# Input:  N:  6
#         Elements: 85 66 3 80 93 88
# Output: 53  (234-181)


n = int(input("Enter N: "))

even_sum = 0
odd_sum = 0

print("Enter elements:")

for i in range(n):
    num = int(input())

    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

difference = even_sum - odd_sum

print("Difference:", difference)