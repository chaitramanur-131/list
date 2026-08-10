count=0
employee_salary=[40000,50000,20000,60000,10000,72000]
print("salary:",employee_salary)
highest_salary=max(employee_salary)
print("highest:",highest_salary)
lowest_salary=min(employee_salary)
print("lowest:",lowest_salary)
total=sum(employee_salary)
print("total:",total)
average=total/6
print("average",average)
for salary in employee_salary:
    if salary > 30000:
        count+=1
print("count",count)
