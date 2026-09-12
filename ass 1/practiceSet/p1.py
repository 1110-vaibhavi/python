amount=int(input("Enter amount to be Withdraw :"))
remaining_amount=amount
notes_10=remaining_amount // 10
remaining_amount %= 10

notes_5= remaining_amount // 5
remaining_amount %= 5

notes_1 = remaining_amount 
print(f"\n To Withdraw {amount}, the cashier will give:")
print(f"Rs. 10 notes : {notes_10}")
print(f"Rs. 5 notes : {notes_5}")
print(f"Rs. 1 notes : {notes_1}")
print(f"Total notes given : {notes_10 + notes_5 + notes_1}")
