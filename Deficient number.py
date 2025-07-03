org = int (input("Enter a number: "))
num = org
d_sum = 0
for i in range(1,num):
    if(num % i == 0):
        d_sum+=i
if(d_sum<org):
    print(org,"is Deficient")
else:
    print(org,"is not Deficient")
