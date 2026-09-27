str="restart"
first_char= str[0]
modified_str=str.replace(first_char,'$')
result=first_char+modified_str[1:]
print(result)