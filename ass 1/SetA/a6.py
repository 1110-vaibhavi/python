num=int(input("Enter any number:"))
temp=num
last_digit=num%10
while num>=10:
    num=num//10
first_digit=num
totalsum=first_digit+last_digit
print(f"First_digit:{first_digit}")
print(f"Last_digit:{last_digit}")
print(f"sum={totalsum}")