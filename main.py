from Employee import *
from Manager import *
from Shift import *
from Roster import *
from Roster import *
from Object import *
from Person import *

# Initialise the main roster object

employees = []
shifts = []

while True:
    print("\n--- Main Menu ---")
    print("1: Create new employee")
    print("2: Create new shift")
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
        required_qualifications = input("Enter required qualifications: ")
        shift = Shifts(shift_day, shift_start, shift_end, required_qualifications)
        shifts.append(shift)
        print(f" Shift on {shift_day} from {shift_start} to {shift_end} created.")

    elif choice == 3:
        pass
    elif choice == 4:
        print(" Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
