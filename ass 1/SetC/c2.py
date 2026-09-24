def invoicebilling():
    '''Invoice Billing with discount and GST'''
    print("----Online shopping Potral----")
    p=float(input("Enter Product Price:"))
    discount=p*10/100
    discounted_price=p-discount
    gst=discounted_price*18/100
    finalbill=discounted_price+gst
    print("----final bill----")
    print(f"original Product price:{p:.2f}")
    print(f"discout on product:{discount:.2f}")
    print(f"Discounted Price:{discounted_price:.2f}")
    print(f"GST applied :{gst}")
    print(f"Your Finall bill :{finalbill}")

if __name__=="__main__":
    invoicebilling()

