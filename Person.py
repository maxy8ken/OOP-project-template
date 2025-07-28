from Object import *
class Person(Object):
    def __init__(self, name, contact_info):
        super().__init__(name)
        self.contact_info = contact_info


    def info(self):
        return f"My name is {self.name} and you can contact me at {self.contact_info}"

    @property
    def contact_info(self):
        return self._contact_info
    
    @contact_info.setter
    def contact_info(self, contact_info):
        self._contact_info = contact_info

e = Person("max","maxdabs")
print(e.info())
e.contact_info = "maxdabsepicly@gmail.com"
print(e.info())