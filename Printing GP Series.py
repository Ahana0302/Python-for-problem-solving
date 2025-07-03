a = int(input("Enter the first term: "))
tn = int(input("Enter the last term: "))
r = int(input("Enter the common ratio: "))

term = a

while (term <= tn):
    print(term, end=" ")
    term = term * r
