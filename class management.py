import pandas as pd 
from collections import namedtuple 
# Define the Employee namedtuple 
Employee = namedtuple("Employee", ["emp_id", "name", "position", 
"salary"]) 
class EmployeeManagementSystem: 
def __init__(self, file_path): 
self.file_path = file_path 
self.load_employees() 
def load_employees(self): 
try: 
self.employees = pd.read_csv(self.file_path) 
except FileNotFoundError: 
self.employees = pd.DataFrame(columns=["Employee ID", 
"Name", "Position", "Salary"]) 
def save_employees(self): 
self.employees.to_csv(self.file_path, index=False) 
def add_employee(self, emp_id, name, position, salary): 
new_employee = pd.DataFrame([[emp_id, name, position, salary]], 
columns=self.employees.columns) 
self.employees = self.employees.append(new_employee, 
ignore_index=True) 
def delete_employee(self, emp_id): 
self.employees = self.employees[self.employees["Employee 
ID"] != emp_id] 
def display_employees(self): 
print(self.employees) 
def menu(): 
print("Employee Management System") 
print("1. Add Employee") 
print("2. Delete Employee") 
print("3. Display Employees") 
print("4. Exit") 
def get_valid_input(prompt, input_type): 
while True: 
try: 
user_input = input(prompt) 
if input_type == "int": 
return int(user_input) 
elif input_type == "float": 
return float(user_input) 
elif input_type == "str": 
return user_input 
except ValueError: 
print("Invalid input! Please enter a valid value.") 
def add_employee(emp_sys): 
try: 
emp_id = int(input("Enter Employee ID: ")) 
name = input("Enter Employee Name: ") 
position = input("Enter Employee Position: ") 
while True: 
salary_input = input("Enter Employee Salary: ") 
try: 
salary = float(salary_input) 
break 
except ValueError: 
print("Invalid input! Salary must be a number.") 
emp_sys.add_employee(emp_id, name, position, salary) 
print("Employee added successfully!") 
except ValueError: 
print("Invalid input! Please enter valid details.") 
def delete_employee(emp_sys): 
print("\nEnter the ID of the employee to delete:") 
emp_id = get_valid_input("Enter Employee ID: ", "int") 
emp_sys.delete_employee(emp_id) 
print("Employee deleted successfully!") 
def main(): 
file_path = "employees.csv"  # Change this to your desired file path 
emp_sys = EmployeeManagementSystem(file_path) 
while True: 
menu() 
choice = get_valid_input("Enter your choice: ", "int") 
if choice == 1: 
add_employee(emp_sys) 
elif choice == 2: 
delete_employee(emp_sys) 
elif choice == 3: 
emp_sys.display_employees() 
elif choice == 4: 
emp_sys.save_employees() 
print("Exiting...") 
break 
else: 
print("Invalid choice! Please enter a valid option.") 
if __name__ == "__main__": 
main()
