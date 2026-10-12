set_a={1,2,3,4,5}
set_b={4,5,6,7,8}

difference_op=set_a-set_b
print("Difference (A-B):",difference_op)

#function
difference_method=set_a.difference(set_b)

symmetric_difference_op=set_a^set_b
print("symmetric Difference (A^B):",symmetric_difference_op)

#function
difference_method=set_a.symmetric_difference(set_b)