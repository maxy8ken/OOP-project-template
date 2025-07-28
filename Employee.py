from Person import *
class Employee(Person):
    def __init__(self, name, contact_info, hours_worked, pay_rate, qualifications = []):
        super().__init__(name, contact_info)
        self.hours_worked = hours_worked
        self.pay_rate = pay_rate
        self.qualifications = qualifications

    @property
    def hours_worked(self):
        return self.hours_worked
    
    @hours_worked.setter
    def hours_worked(self, hours_worked):
        self._hours_worked = hours_worked

    @property
    def pay_rate(self):
        return self.pay_rate
    
    @pay_rate.setter
    def pay_rate(self, pay_rate):
        self._pay_rate = pay_rate
    
    @property
    def qualifications(self):
        return self.qualifications
    
    @qualifications.setter
    def qualifications(self, qualifications):
        self._qualifications = qualifications
    

