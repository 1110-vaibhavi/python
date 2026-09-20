num=int(input("Enter any number:"))
temp=num
sum=0
even=0
odd=0
zeros=0

while num>0:
    rem=num%10
    sum= sum+rem
    num=num//10
    if num%2==0:
        even +=1
    elif num==0:
        zeros +=1
    else:
        odd +=1
print(f"Cout of even numbers:{even}")
print(f"Count of odd number is :{odd}")
print(f"Cout of zeros numbers:{zeros}")