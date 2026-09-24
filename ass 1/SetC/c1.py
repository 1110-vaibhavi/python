def get_grade_point(marks):
    """Coverts percentage marks into  the corresponding grade point"""
    if 90<+marks<+100:
        return 10
    elif 80<=marks<90:
        return 9
    elif 70<=marks<79:
        return 8
    elif 60<=marks<70:
        return 7
    elif 50<=marks<60:
        return 6
    elif 45<=marks<50:
        return 5
    elif 40<=marks<45:
        return 4
    elif 0<=marks<40:
        return 0
    else:
        print("Marks Must be between 0 to 100")

def calculate_gpa():
    print("----University Gpa Calculater----")
    grade_points=[]
    for i in range(1,6):
        while True:
            marks=float(input(f"Enter /marks obtain in subject {i} (0-100)"))
            if 0<=marks<=100:
                gp=get_grade_point(marks)
                grade_points.append(gp)
                break
            else:
                print("Invalid input.")

    total_gp=sum(grade_points)
    gpa=total_gp/5
    print("\n ---Summary Result---")
    for i,g in enumerate(grade_points,1):
        print(f"Subject {i} Grade Points: {g}")
    print(f"\nFinal Calculated Gpa:{gpa:.2f}")
if __name__=="__main__":
    calculate_gpa()