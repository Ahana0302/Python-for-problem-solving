num = int(input("Enter a number"))
temp = num
sum_of_digits = 0

while(temp>0):
    d = temp % 10
    sum_of_digits = sum_of_digits + d
    temp = temp // 10
   
if num % sum_of_digits == 0:
    print("Is a Harshad number")
else:
    print("Is not a Harshad number")
        
    
