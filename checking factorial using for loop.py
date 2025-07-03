n = int(input("Enter a number: "))
fact = 1

if n < 0:
    print("Factorial is not defined.")
else:
    for i in range(n, 0, -1):
        fact *= i
    print("Factorial is", fact)
