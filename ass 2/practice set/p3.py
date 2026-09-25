vowels=0
consonents=0
string=str(input("enter your string:"))
for ch in string:
    if ch in "aeiou":
        vowels +=1
    else:
        consonents +=1

print("vowels count:",vowels)
print("consonents:",consonents)