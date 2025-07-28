from Employee import *
from Manager import *
from Shift import *
from Roster import *
from Object import *
from Person import *


while True:
    print("1: Create new roster")
    print("2: Create new employee")
    print("3: Create new manager")
    print("4: Create new shift")
    print("5: Assign employee to shift")
    choice = int(input("What would you like to do? "))
    if choice == 1:
        break
    if choice == 2:
        employeename = input("What is the employee's name? ")
        employeecontact = input("What is the employee's contact info? ")
        employeePayRate = input("What is the employee's pay rate? ")
        employeename = Employee(employeename, employeecontact, 0, employeePayRate)
    if choice == 3:
        break
    if choice == 4:
        break
    if choice == 5:
        break