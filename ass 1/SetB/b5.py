start=int(input())
end=int(input())
print(f"Multiplication tables from {start} to {end}")
for num in range(start,end+1):
    print(f"----table of {num}----")
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
    print()