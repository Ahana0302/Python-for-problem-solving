row = int(input("Enter the size: "))
for i in range (row, 0, -1):
         for k in range(row - i):
              print(" ",end=" ")
         for j in range(1, i + 1):
              print("* ",end="")
         print()
 
