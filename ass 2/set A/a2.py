string=str(input("Enter your string:"))
dict={}
for ch in string:
    dict[ch]=dict.get(ch,0)+1
print("Expected Result:",dict)