num=int(input("Enter any number:"))
temp=num
sum=0
while num>0:
    rem=num%10
    sum= sum+rem
    num=num//10
print(f"the sum of the digits of {temp} is : {sum}")