 Programming Practices in Rostering Tool Project

This document outlines the good programming practices used in the development of the Rostering Tool Project, supported by descriptions and code snippets.


 1. Clear and Uncluttered Mainline

Description:
The main.py file serves as a high-level controller, delegating logic to separate modules and maintaining a clean structure.

Why:
Helps improve readability, testing, and modularity.

```python
from Employee import *
from Manager import *
from Shift import *
from Roster import *
from Object import *
from Person import *

# Initialise the main roster object
main_roster = Roster()
employees = []
shifts = []

while True:
    print("\n--- Main Menu ---")
    print("1: Create new employee")
    print("2: Create new shift")
    print("3: Assign employee to shift")
    print("4: Exit")

    choice = int(input("What would you like to do? "))

    if choice == 1:
        employeename = input("What is the employee's name? ")
        employeecontact = input("What is the employee's contact info? ")
        employeePayRate = float(input("What is the employee's pay rate? "))
        employee = Employee(employeename, employeecontact, 0, employeePayRate)
        employees.append(employee)
        print(f" Employee '{employeename}' created.")

    elif choice == 2:
        shift_day = input("Enter the day of the shift (e.g. Monday): ")
        shift_start = input("Enter start time (e.g. 09:00): ")
        shift_end = input("Enter end time (e.g. 17:00): ")
        shift = Shift(shift_day, shift_start, shift_end)
        shifts.append(shift)
        print(f" Shift on {shift_day} from {shift_start} to {shift_end} created.")

    elif choice == 3:
        if not employees or not shifts:
            print(" You must create at least one employee and one shift first.")
            continue

        print("\nAvailable Employees:")
        for idx, emp in enumerate(employees):
            print(f"{idx + 1}: {emp.name}")

        emp_index = int(input("Select employee by number: ")) - 1

        print("\nAvailable Shifts:")
        for idx, sh in enumerate(shifts):
            print(f"{idx + 1}: {sh.day} from {sh.start_time} to {sh.end_time}")

        shift_index = int(input("Select shift by number: ")) - 1

        main_roster.assign_employee_to_shift(employees[emp_index], shifts[shift_index])
        print(f"Assigned {employees[emp_index].name} to {shifts[shift_index].day} shift.")

    elif choice == 4:
        print(" Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
```


 2. One Logical Task per Subroutine

Description:
Each function within the imported classes handles a specific task, such as creating an employee or assigning a shift.

Why:
Improves modularity, reuse, and ease of debugging.

> Example (within Employee and Roster classes):
```python
# Inside Employee class
class Employee(Person):
    def __init__(self, name, contact_info, hours_worked, pay_rate):
        super().__init__(name, contact_info)
        self.hours_worked = hours_worked
        self.pay_rate = pay_rate

# Inside Roster class
class Roster:
    def assign_employee_to_shift(self, employee, shift):
        shift.assign_employee(employee)
```


 3. Use of Stubs

Description:
Stub methods were used during development to allow mainline testing before full implementation.

Why:
Allowed testing the menu interface and object interactions before backend logic was complete.

```python
# In Shift.py or Roster.py
class Shift:
    def assign_employee(self, employee):
        # Stub implementation
        print(f"Stub: Assigned {employee.name} to shift.")
```



 4. Use of Control Structures and Data Structures

Description:
The mainline uses loops, conditionals, and custom data structures (lists, classes).

Why:
Manages program flow and user interaction efficiently.

```python
while True:
    print("\n--- Main Menu ---")
    # ...
    if choice == 1:
        # Create employee
    elif choice == 2:
        # Create shift
    elif choice == 3:
        # Assign shift
    elif choice == 4:
        break
```

```python
employees = []  # list of Employee objects
shifts = []     # list of Shift objects
```



 5. Ease of Maintenance

Description:
Modular codebase with separate files (e.g. Employee.py, Roster.py) and descriptive variable names.

Why:
Easy to update logic or expand with new features (e.g., exporting rosters).

```python
employee = Employee(employeename, employeecontact, 0, employeePayRate)
main_roster.assign_employee_to_shift(employee, shift)
```


 6. Version Control

Description:
Project tracked using Git. Each feature or fix was committed separately with clear messages.

Why:
Enables team collaboration and rollback.

Example Git Log:
```
commit 7c81a2e - Add input validation to shift assignment
commit 3fae21e - Implement Roster assign logic
commit 84bd201 - Create menu loop and class imports
```



 7. Regular Backups

Description:
Backed up regularly to GitHub and exported zip to external drive.

Why:
Protection from data loss or accidental overwrite.

Example:
- GitHub commit history 
- Weekly ZIP folder archived on Google Drive



