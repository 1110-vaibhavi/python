string=input("Enter your string :")
substring=string[0]+string[1]+string[-2]+string[-1]
if len(substring) < 2:
   print("empty string")
else:
    print(substring)