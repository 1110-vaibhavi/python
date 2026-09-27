string=str(input("Enter your string:"))
string1=""
for i ,char in enumerate(string):
    if i % 2 == 0:
        string1 += char
print("By the first way:")
print(string1)
print("by the scond way:")
string2=string[::2]
print(string2)