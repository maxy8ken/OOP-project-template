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
