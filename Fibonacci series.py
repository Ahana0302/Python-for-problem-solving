x = 0
y = 1
Next = 0
term = int (input("Enter a number: "))
print("Fibonacci series upto",term,"terms:")
for i in range(term):
    print(x,end=" ")
    Next = x + y
    x = y
    y = Next
