import json
import os

employee1 = {
    "employee_id":"EMP101", 
    "name":"Priyan", 
    "age":32, 
    "department":"IT", 
    "salary":75000, 
    "currently_working":True
    }
employee2 = {
    "employee_id":"EMP102", 
    "name":"Rahul", 
    "age":28, 
    "department":"Finance", 
    "salary":45000, 
    "currently_working":True
    }
employee3 = {
    "employee_id":"EMP103", 
    "name":"Ananya", 
    "age":25, 
    "department":"HR", 
    "salary":55000, 
    "currently_working":True
    }
employee4 = {
    "employee_id":"EMP104", 
    "name":"Sneha", 
    "age":26, 
    "department":"Marketing", 
    "salary":50000, 
    "currently_working":True
    }

def save_employees():
    with open("employees.json", "w") as file:
        json.dump(employees, file)

if os.path.exists("employees.json"):
    with open("employees.json", "r") as file:
        employees = json.load(file)
else:
    employees = [employee1, employee2, employee3, employee4]
    save_employees()
              
def display_menu():
    print("=========Employee Management System===========")
    print("1. Display all employees")
    print("2. Search employees")
    print("3. Add employees")
    print("4. Change department")
    print("5. Remove employees")
    print("6. Calculate Salary")
    print("7. Exit")

def display_employee():
    for employee in employees:
        print(employee)

def search_employee():
    search_employee_id = input("Enter an Employee ID:")
    search_employee_id = search_employee_id.strip()
    for employee in employees:
        if employee["employee_id"] == search_employee_id:
            print(f"Employee Found: {employee['name'], employee['department'], employee['salary']}")
            break
    else:
        print("Employee not found") 

def valid_id():
    while True:
        new_employee_id = input("Enter an employee id:")
        new_employee_id = new_employee_id.strip()
        if new_employee_id == "":
            print("please enter valid id")
            continue
        else:
            employee_id = new_employee_id[3:]
            if new_employee_id.startswith("EMP") and employee_id.isdigit():
                return new_employee_id
            else:
                print("Please enter valid id")

def valid_name():
    while True:
        new_employee_name = input("enter employee name:")
        new_employee_name = new_employee_name.strip()
        if new_employee_name == "":
            print("Please enter valid name")
            continue

        else:
            name_list = new_employee_name.split()
            if all(name.isalpha() for name in name_list):
                return new_employee_name
            else:
                print("Please enter valid name")
                continue       
        
def valid_age():
    while True:
        new_employee_age = input("Enter employee age:")
        try:
            new_employee_age = int(new_employee_age)
        except ValueError:
            print("Please enter vallid age")
            continue

        if new_employee_age > 60 or new_employee_age < 20:
            print("Please Enter age between 20 - 60")
        else:
            return new_employee_age

def valid_salary():
    while True:
        new_employee_salary = input("Enter employee salary:")
        try:
            new_employee_salary = int(new_employee_salary)
        except ValueError:
            print("Please enter vallid salary")
            continue

        if new_employee_salary <= 10000:
            print("Please Enter valid salary")
        else:
            return new_employee_salary

def valid_dept():
    while True:
        new_employee_department = input("Enter employee department:")
        new_employee_department = new_employee_department.strip()
        if new_employee_department == "":
            print("Please enter valid department")
            continue
        department = new_employee_department.split()
        if all(dept.isalpha() for dept in department):
            return new_employee_department
        else:
            print("Please Enter valid department")

def valid_working_status():
    while True:
        new_employee_working = input("Enter True/False:")
        new_employee_working = new_employee_working.strip().lower()

        if new_employee_working == "true":
            return True
        elif new_employee_working == "false":
            return False
        else:
            print("Please enter (true/false)")
            continue

def add_employee():
    while True:
        new_employee_id = valid_id()
        for employee in employees:
            if employee["employee_id"] == new_employee_id:
                print("Employee_ID already exists")
                break
        else:
            break
    new_employee_name = valid_name()
    new_employee_age = valid_age()
    new_employee_department = valid_dept()
    new_employee_salary = valid_salary()
    new_employee_working = valid_working_status()

    new_employee = {
        "employee_id": new_employee_id,
        "name": new_employee_name,
        "age": new_employee_age,
        "department": new_employee_department,
        "salary": new_employee_salary,
        "currently_working": new_employee_working,
    }

    employees.append(new_employee)
    save_employees()

    print("employee added successfully")
    print(employees)
 
def change_department():
    search_employee_id = input("Enter an Employee ID:")
    search_employee_id = search_employee_id.strip()
    for employee in employees:
        if employee["employee_id"] == search_employee_id:
            print(f"Employee Found: {employee['name'], employee['department'], employee['salary']}")
            new_department = valid_dept()
            employee["department"] = new_department
            save_employees()
            print(employee["department"])
            print(employee)
            break
    else:
        print("Employee not found")

def remove_employee():
    search_employee_id = input("Enter an Employee ID:")
    search_employee_id = search_employee_id.strip()
    for employee in employees:
        if employee["employee_id"] == search_employee_id:
            print(f"Employee Found: {employee['name'], employee['department'], employee['salary']}")
            employees.remove(employee)
            save_employees()
            print("Employee deleted successfully")
            print(employees)
            break
    else:
        print("Employee not found") 

def valid_bonus():
    while True:
        bonus_amount = input("Enter bonus amount:")
        try:
            bonus_amount = int(bonus_amount)
        except ValueError:
            print("Please Enter valid bonus amount")
            continue
        if bonus_amount < 0:
            print("Please Enter valid bonus amount")
            continue
        else:
            return bonus_amount

def valid_deduction():
    while True:
        deduction_amount = input("Enter deduction amount:")
        try:
            deduction_amount = int(deduction_amount)
        except ValueError:
            print("Please Enter valid deduction amount")
            continue
        if deduction_amount < 0:
            print("Please Enter valid deduction amount")
            continue
        else:
            return deduction_amount

def calculate_salary():
    search_employee_id = input("Enter an Employee ID:")
    search_employee_id = search_employee_id.strip()
    for employee in employees:
        if employee["employee_id"] == search_employee_id:
            print(f"Employee Found: {employee['name'], employee['department'], employee['salary']}")
            bonus_amount = valid_bonus()
            deduction_amount = valid_deduction()
            final_salary = employee["salary"] + bonus_amount - deduction_amount
            print(f"Employee Salary:{employee['salary']}, Bonus:{bonus_amount}, Deduction:{deduction_amount}, Final Salary:{final_salary}")
            break
    else:
        print("Employee not found")

def valid_choice():
    while True:
        choice = input("Enter your choice:")
        try:
            choice = int(choice)
        except ValueError:
            print("Please Enter valid choice")
            continue

        if choice > 7 or choice < 1:
            print("Please Enter number between 1 and 7")
        else:
            return choice

while True:
    display_menu()
    choice = valid_choice()
    if choice == 1:
        display_employee()
    elif choice == 2:
        search_employee()
    elif choice == 3:
        add_employee()
    elif choice == 4:
        change_department()
    elif choice == 5:
        remove_employee()
    elif choice == 6:
        calculate_salary()
    elif choice == 7:
        print("Thankyou for using Employee Management System")
        break




# bonus = 5000
# deduction = 2000

# annual_salary = salary * 12
# additional_bonus = salary + bonus
# salary_deduction = salary - deduction

# print("Name:", name)
# print("Age:", age)
# print("Department:", department)
# print("Salary:", salary)
# print("Currently Working:", currently_working)
# print("Annual Salary:", annual_salary)
# print("Bonus:", additional_bonus)
# print("Salary Deduction:", salary_deduction)
# print("Salary greater than 50000:", salary > 50000)
# print("Salary equals to 75000:", salary == 75000)
# print("Salary less than 40000:", salary < 40000)
# print("Salary not equals to 60000:", salary != 60000)

# print("salary greater than 50000 and currently working:", salary > 50000 and currently_working)
# print("salary greater than 100000 or currently working:", salary > 100000 or currently_working)
# print("priyan not currently woking:", not currently_working)

# if salary > 70000:
#     print("Employee is Eligible for high bonus")
# elif salary > 50000:
#     print("Employee is Eligible for standard bonus")
# else:
#     print("Employee is not Eligible for bonus")

# if currently_working:
#     if salary > 50000:
#         print("Employee is Eligible for bonus")
#     else:
#         print("Employee is not Eligible for bonus")
# else:
#     print("Employee is not working")

# for i in range(5):
#     print("Employee record processed")

# employees = ["Priyan", "Rahul", "Ananya", "Kiran", "Sneha"]

# for employee in employees:
#     print("Welcome", employee)

# for employee in employees:
#     if len(employee) > 5:
#         print(employee)

# print(len(employees))

# for employee in employees:
#     print(employee)

# for employee in employees:
#     print(f"{employee} character:", len(employee))

# for employee in employees:
#     if len(employee) >= 6:
#         print(employee)

# count = 1
# while count <= 3:
#     password = input("Enter a password:")
#     if password == "engineering":
#         print("login successfull")
#         break
#     else:
#         print("please enter correct password")
#     count = count + 1

# for employee in employees:
#     if employee == "Rahul":
#         break
#     print(employee)

# for employee in employees:
#     if employee == "Ananya":
#         continue
#     print(employee)

# count = 0
# while count < 5:
#     if employees[count] == "Ananya":
#        break
#     print(employees[count])
#     count = count + 1

# count = 0
# while count < len(employees):
#     if employees[count] == "Ananya": 
#         count = count + 1   
#         continue
#     print(employees[count])
#     count = count + 1  

# first_name = "Priyan"
# last_name = "Kumar"
# full_name = first_name + " " + last_name
# print(full_name)

# employee_name = "     priyan kumar            "
# employee_name = employee_name.strip()
# print(employee_name)

# employee_name = employee_name.replace("kumar", "sharma")
# print(employee_name)

# print(employee_name.capitalize())
# employee_name = employee_name.title()
# print(employee_name)


# print(len(employee_name))

# department = "it"
# print(department.upper())

# name = "Priyan Kumar"
# seperated_name = name.split()
# print(seperated_name)

# date = "25-11-2004"
# custom_split = date.split("-")
# print(custom_split)

# department = ["IT", "HR", "Finance"]
# all_department = ", ".join(department)
# print(all_department)

# employee_id = "EMP205"
# print(employee_id.startswith("EMP"))
# print(employee_id.endswith("205"))
# print(employee_id.index("205"))
# print(employee_id.count("0"))

# employees = ["Priyan", "Rahul", "Ananya", "Kiran", "Sneha"]
# employees[1] = "Rohit"
# employees[4] = "Shruti"
# print(employees)

# employees = ["Priyan", "Rohit", "Ananya", "Kiran"]
# employees.append("Meera")
# print(employees)

# employees = ["Priyan", "Rohit", "Ananya", "Kiran"]
# employees.insert(1, "Meera")
# print(employees)

# employees = ["Priyan", "Rohit", "Ananya"]
# new_employees = ["Meera", "Sneha"]
# employees.extend(new_employees)
# print(employees)

# employees = ["Priyan", "Rahul", "Ananya", "Kiran", "Kiran", "Sneha"]
# employees.remove("Kiran")
# print(employees)

# employees = ["Priyan", "Rahul", "Ananya", "Kiran", "Sneha"]
# employee_removed = employees.pop(1)
# print(employee_removed)
# print(employees)

# employees = ["Priyan", "Rahul", "Kiran", "Ananya", "Kiran", "Sneha"]
# employees.remove("Kiran")
# employees.remove("Kiran")
# print(employees)

# employees = ["Priyan", "Rahul", "Ananya", "Kiran"]
# del employees[2]
# print(employees)

# employees = ["Priyan", "Rahul", "Ananya", "Kiran"]
# employees.clear()
# print(employees)

# employees = ["Sneha", "Ananya", "Priyan", "Kiran", "Rahul"]
# employees.sort()
# print(employees)

# employees = ["Sneha", "Rahul", "Priyan", "Kiran", "Ananya"]
# employees.sort(reverse=True)
# print(employees)

# employees = ["Priyan", "Rahul", "Kiran", "Rahul", "Ananya", "Rahul"]
# print(employees.count("Rahul"))

# employees = ["Priyan", "Rahul", "Kiran", "Rahul", "Ananya", "Rahul"]
# employees_count = employees.count("Rahul")
# print(employees_count)

# employees = ["Priyan", "Rahul", "Kiran", "Ananya", "Rahul"]
# print(employees.index("Rahul"))

# employees = ["Priyan", "Rahul", "Ananya", "Kiran"]
# backup_employees = employees.copy()

# employees.append("Meera")
# print(employees)
# print(backup_employees)

# employees = ["Priyan", "Rahul", "Ananya", "Kiran"]
# print("Ananya" in employees)
# print("Meera" not in employees)

# employees = ["Priyan", "Rahul", "Ananya", "Kiran"]
# employees.append("Meera")

# employees.insert(2, "Sneha")

# employees.remove("Rahul")

# print("Ananya" in employees)

# print(employees.count("Priyan"))

# employees.sort()

# backup_employees = employees.copy()

# print(employees)
# print(backup_employees)

# employee_details = ("Priyan", 32, "IT")
# print(employee_details[1])

# employees = ["Priyan", "Rahul", "Ananya", "Kiran"]
# print(employees[1])

# employee_details = ("Priyan", 32, "IT")
# employee_details[1] = 35

# departments = ("IT", "HR", "IT", "Finance", "IT")
# print(departments.count("IT"))
# print(departments.index("Finance"))

# employee = ("Rahul", 28, "Finance")
# name, age, department = employee
# print(name)
# print(age)
# print(department)

# employee = ("Rahul", 28, "Finance", "EMP102", 45000)
# print(employee[0])
# print(employee[-1])
# print(len(employee))
# name, age, department, employee_id, salary = employee
# print(salary)

# departments = {"IT", "HR", "Finance", "IT", "Sales", "HR", "Finance", "Marketing", "IT"}
# print(departments)
# print(len(departments))

# employees = ["Priyan", "Rahul", "Ananya", "Kiran"]
# employees_converted = set(employees)
# print(employees_converted)

# numbers = (10, 20, 10, 30, 20)
# numbers_converted = set(numbers)
# print(numbers_converted)

# empty_set = set()
# print(type(empty_set))

# empty_dictionary = {}
# print(type(empty_dictionary))

# departments = {"IT", "HR", "Finance"}
# departments.add("Security")
# departments.add("Marketing")
# departments.add("IT")
# print(len(departments))

# print(departments)

# departments = {"IT", "HR", "Finance", "Sales"}
# departments.remove("Finance")
# departments.discard("Sales")
# departments.discard("Marketing")

# print(departments)

# departments = {"IT", "HR", "Finance"}
# departments.update(["Security", "Marketing", "Sales", "IT"])

# print(departments)
# print(len(departments))

# departments = {"IT", "HR", "Finance"}
# print("IT" in departments)
# print("Finance" not in departments)

# departments = {"IT", "HR", "Finance"}
# departments.clear()
# print(departments)
# print(len(departments))
# print(type(departments))

# departments = {"IT", "HR", "Finance"}
# backup_departments = departments.copy()
# departments.remove("HR")

# print(departments)
# print(backup_departments)

# python_employees = {"Rahul", "Ananya", "Kiran"}
# java_employees = {"Priyan", "Ananya", "Sneha"}

# all_employees = python_employees.union(java_employees)
# another_employees = python_employees | java_employees
# print(all_employees)
# print(another_employees)

# python_employees = {"Rahul", "Ananya", "Kiran", "Meera"}
# java_employees = {"Priyan", "Ananya", "Meera", "Sneha"}
# common_employees = python_employees.intersection(java_employees)
# same_employees = python_employees & java_employees

# print(common_employees)
# print(same_employees)

# python_employees = {"Rahul", "Ananya", "Kiran", "Meera"}
# java_employees = {"Priyan", "Ananya", "Meera", "Sneha"}

# difference = python_employees.difference(java_employees)
# difference_again = python_employees - java_employees
# print(difference)
# print(difference_again)

# python_employees = {"Rahul", "Ananya", "Kiran", "Meera"}
# java_employees = {"Priyan", "Ananya", "Meera", "Sneha"}

# symmetric_difference = python_employees.symmetric_difference(java_employees)
# again_symmetric = python_employees ^ java_employees
# print(symmetric_difference)
# print(again_symmetric)

# A = {10, 20, 30, 40}
# B = {30, 40, 50, 60}

# union = A.union(B)
# intersection = A & B
# difference = A.difference(B)
# symmetric_difference = A ^ B

# print(union)
# print(intersection)
# print(difference)
# print(symmetric_difference)

# company_departments = {"IT", "HR", "Finance", "Sales"}
# training_departments = {"IT", "HR"}
# subset = training_departments.issubset(company_departments)
# subset_another = company_departments.issubset(training_departments)
# print(subset)
# print(subset_another)

# company_departments = {"IT", "HR", "Finance", "Sales"}
# training_departments = {"IT", "HR"}
# superset = training_departments.issuperset(company_departments)
# superset_another = company_departments.issuperset(training_departments)
# print(subset)
# print(subset_another)

# python_employees = {"Rahul", "Ananya", "Kiran"}
# java_employees = {"Priyan", "Sneha", "Meera"}
# disjoint = python_employees.isdisjoint(java_employees)
# print(disjoint)

# python_employees = {"Rahul", "Ananya", "Kiran"}
# java_employees = {"Priyan", "Sneha", "Meera","Rahul"}
# disjoint = python_employees.isdisjoint(java_employees)
# print(disjoint)

# python_employees = {"Rahul", "Ananya", "Kiran"}
# java_employees = {"Priyan", "Sneha", "Meera", "Sneha"}
# disjoint = python_employees.isdisjoint(java_employees)
# print(disjoint)

# departments = {"IT", "HR", "Finance", "Sales"}
# removed = departments.pop()
# print(removed)
# print(departments)

# salaries = [25000, 35000, 45000, 55000, 65000]
# high_salaries = {item for item in salaries if item > 40000}
# print(high_salaries)

# departments = {"IT", "HR", "Finance"}
# departments = frozenset({"IT", "HR", "Finance"})
# print(type(departments))

# departments.add("Sales")
# print(departments)