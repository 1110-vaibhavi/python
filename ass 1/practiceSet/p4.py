cost_price=int(input("Enter cost price : "))
selling_price=int(input("Enter selling price : "))
profit=selling_price-cost_price
loss=cost_price-selling_price

if(selling_price > cost_price):

    print("Profit made up to :",profit,end='rs.')
elif cost_price > selling_price:
    print("Loss made up to :",loss,end='rs.')
else:
    print("No profit ,No loss")
