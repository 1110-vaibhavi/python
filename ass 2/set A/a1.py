list=[]
#iserting the elements in lis
n=int(input("how many elements you want to insert in list:"))
print("Enter Element:")
for i in range(n):
   element=int(input())
   list.append(element)

unique_list=set(list)
if len(unique_list)<len(list):
   print("Duplicates")
else:
   print("all unique")