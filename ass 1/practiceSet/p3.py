x=float(input("Enter the x-coordinate: "))
y=float(input("Enter the y-coordinate: "))
if x>0 and y>0:
    print(f"the point ({x},{y}) lies in Quadrant 1 (+,+)")
elif x < 0 and y>0:
    print(f"the point ({x},{y}) lies in Quadrant 2 (-,+)")
elif x<0 and y<0:
    print(f"the point ({x},{y}) lies in Quadrant 3 (-,-)")
elif x >0 and y<0:
    print(f"the point ({x},{y}) lies in Quadrant 4 (+,-)")
elif x==0 and y==0:
    print(f"the point ({x},{y}) is at Origin (0,0)")
elif x==0:
    print(f"the point ({x},{y}) lies on y Axis")
else:
    print(f"the point ({x},{y}) lies on x axis")