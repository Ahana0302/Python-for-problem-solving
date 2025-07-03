n = int(input("Enter the number of rows: "))
size=n//2+1
for i in range(1, size+1):
    for j in range(1,size-i+1):
        print(" ",end=" ")
    for j in range(1, 2*i):
        print("* ",end="")
    print()        

for i in range(size-1,0,-1):
    for j in range(1,size-i+1):
        print(" ",end=" ")
    for j in range(1, 2*i):
        print("* ",end="")
    print()        
