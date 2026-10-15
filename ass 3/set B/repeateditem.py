tup1=(8,9,5,7,4,9,5,6,4,2,5555,888,999)
seen=set()
repeated=set()
for item in tup1:
    if item in seen:
        repeated.add(item)
    else:
        seen.add(item)
print("Repeated items :",list(repeated))