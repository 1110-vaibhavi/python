num=28
sum=0
temp=num
i=1
while i<num:
    if num%i==0:
        sum += i
    i += 1

if sum==temp:
    print("the number is a perfect number")
else:
    print("the number is not a perfect number")