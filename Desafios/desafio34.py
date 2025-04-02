salary = int(input("qua seu salary? "))
print(salary)
salaryMedia = 1250


if salary > salaryMedia:
    newSalary = salary * 0.1
    salaryFinal = newSalary + salary
    print(f"Your new salary is {salaryFinal}R$ ")
else:
    newSalary = salary * 0.15
    salaryFinal = newSalary + salary
    print(f"Your new salary is {salaryFinal}R$ ")

