from Object import *
def __init__(self,name, shifts=[], employees=[]):
    super().__init__(name)
    self.shifts = shifts
    self.employees = employees


    @property
    def shifts(self):
        return self.shifts
    
    @shifts.setter
    def shifts(self, shifts):
        self._shifts = shifts

    @property
    def employees(self):
        return self.employees
    
    @employees.setter
    def employees(self, employees):
        self._employees = employees
