str1="abc"
str2="xyz"
str3=str1
str1=str1.replace(str1[0],str2[0])
str1=str1.replace(str1[1],str2[1])

str2=str2.replace(str2[0],str3[0])
str2=str2.replace(str2[1],str3[1])
print(str1+" "+str2)