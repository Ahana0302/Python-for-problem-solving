size = int(input("Enter the number of rows: "))
for i in range(size,0,-1):
    for j in range(size-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("* ",end="")
    print()        
