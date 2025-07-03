org = int (input("Enter a number: "))
square = org ** 2
new = 0
while(square!=0):
    digit = square % 10
    new+=digit
    square = square//10

if(org == new):
    print(org,"is a Neon no.")
else:
    print(org,"is not a Neon no.")
