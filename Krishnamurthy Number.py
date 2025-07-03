num = int(input("Enter a number"))
temp = num
sum = 0

while(num>0):
    d = num % 10
    f = 1
    i = 1
    while(i<=d):
        f = f * i
        i = i + 1

    sum = sum + f
    num = num // 10
   
if sum == temp:
    print("Is a Krishnamurthy number")
else:
    print("Is not a Krishnamurthy number")
        
    
