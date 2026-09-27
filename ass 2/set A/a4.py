#stack implimentation with list
stack=[]
while True:
    print("\n------Stack Operation--------")
    print("1. Push (Insert)")
    print("2. Pop (Delete)")
    print("3. Peek (view Top)")
    print("4. Display Stack")
    print("5. Exit")

    choice=input("Enter your choice (1-5):")
    if choice=='1':
       item=input("Enter the value to push:")
       stack.append(item)
       print(f"'{item}' successfully pushed in stack")

    elif choice=='2':
        if len(stack)==0:
            print("Stack Underflow! The stack is already empty.")
        else:
            popped_item=stack.pop()
            print(f"Popped item:{popped_item}")

    elif choice=='3':
        if len(stack)==0:
            print("the stack is empty.")
        else:
            print(f"Top element is :{stack[-1]}")

    elif choice=='4':
        if len(stack)==0:
                    print("the stack is empty.")
        else:
             print("current Stack (top -> bottom:)",stack[::-1])

    elif choice=='5':
        print("Exiting.......")

    else:
         print("invalid choice")
