# Accept number of rows and number of columns from user and display below pattern 
# Input: iRow = 5 , iCol = 5 
# Output: $ * * * * 
#         # $ * * * 
#         # # $ * * 
#         # # # $ * 
#         # # # # $ 


iRow = int(input("Enter number of rows: "))
iCol = int(input("Enter number of columns: "))

for i in range(iRow):
    for j in range(iCol):
        if i == j:
            print("$", end=" ")
        elif j < i:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()