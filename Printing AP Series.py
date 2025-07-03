a = int(input("Enter the first term: "))
tn = int(input("Enter the last term: "))
d = int(input("Enter the common difference: "))

term = a

while (term <= tn):
    print(term, end=" ")
    term = term + d
