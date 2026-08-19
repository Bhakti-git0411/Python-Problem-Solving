# Accept N numbers from the user and check whether that number contains 11 in it or not
# Input:  N:  6
#         Elements: 85 66 11 80 93 88 
# Output: 11 is present


n = int(input("N: "))
elements = list(map(int, input("Elements: ").split()))

if 11 in elements:
    print("11 is present")
else:
    print("11 is not present")