num = int(input("Enter a number: "))
sum_d = 0
while(num>0):
    digit = num % 10
    sum_d += digit
    num = num // 10
print(sum_d)
