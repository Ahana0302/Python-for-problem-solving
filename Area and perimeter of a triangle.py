import math
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))
peri = (a + b + c)
s = 0.5 * peri
area = math.sqrt(s *(s-a)*(s-b)*(s-c))
print("The Perimeter is: ",peri)
print("The Area is: ",area)
