d1={'a':100,'b':200}
d2={'a':200,'b':100}
combined_dict={key:d1[key]+d2[key]for key in d1}
print(combined_dict)