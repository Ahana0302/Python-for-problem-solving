size = int(input("Enter the number of rows: "))
for i in range(1, size+1):
    for j in range(size-i):
        print(" ",end=" ")
    for k in range(1, 2*i):
        print("* ",end="")
    print()        
