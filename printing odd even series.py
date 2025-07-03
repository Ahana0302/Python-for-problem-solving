n = int(input("Enter the last term: "))

print("Even natural numbers: ")
for i in range(1,n+1):
    if i % 2 == 0:
        print(i, end=" ")

print("\nOdd natural numbers: ")
for i in range(1,n+1):
    if i % 2 != 0:
        print(i, end=" ")
    
