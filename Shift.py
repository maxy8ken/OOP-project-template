from Object import *
from Roster import *
class Shifts(Object):
    def __init__(self, day, start_time, end_time, required_qualifications, assigned_employee=[], employees=[]):
        super().__init__(employees)
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.required_qualifications = required_qualifications
        self.assigned_employee = assigned_employee

    def assign_employee(self, employees, i):
        self.assigned_employee = employees[i].append
    
    
    def isShiftFilled(self, i):
        if self.assigned_employee == True:
            return f"Yes {self.employees[i]} is working the shift"
        else:
            return f"no one is working this shift"

    @property
    def day(self):
        return self.day
    
    @day.setter
    def day(self, day):
        self._day = day

    @property
    def start_time(self):
        return self.start_time
    
    @start_time.setter
    def start_time(self, start_time):
        self._start_time = start_time

    @property
    def end_time(self):
        return self.end_time
    
    @end_time.setter
    def end_time(self, end_time):
        self._end_time = end_time

    @property
    def required_qualifications(self):
        return self.required_qualifications
    
    @required_qualifications.setter
    def required_qualifications(self, required_qualifications):
        self._required_qualifications = required_qualifications

    