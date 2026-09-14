num=int(input("Enter any number:"))
temp=num
rem=0
sum=0
while(num>0):
    rem=num % 10
    sum= sum+(rem*rem*rem)
    num = num // 10
if(sum==temp):
    print("the number is armstrong")
else:
    print("the number is not armstrong")