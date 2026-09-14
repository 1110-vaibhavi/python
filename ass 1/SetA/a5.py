n=int(input("Enter number : "))
temp=n
reversedno=0
while(n > 0):
    reminder= n % 10
    reversedno = (reversedno*10)+reminder
    n //= 10
if(temp == reversedno):
    print("The no. is palindrom")
else:
    print("The no is not palindrom")