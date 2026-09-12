basic_salary=float(input("Enter Employes Basic Salary : "))
if basic_salary < 250000 :
    income_tax= 0.0
elif basic_salary > 250000 or basic_salary < 500000 :
    income_tax= basic_salary*0.1
elif basic_salary > 500000 :
    income_tax=basic_salary*0.2

