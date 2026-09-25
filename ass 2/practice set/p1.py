list=[]
#iserting the elements in lis
n=int(input("how many elements you want to insert in list:"))
print("Enter Element:")
for i in range(n):
   element=int(input())
   list.append(element)

print("the list is :")
print(list)
#reversing the elements in list
print("the reverse list is :",list[::-1])
