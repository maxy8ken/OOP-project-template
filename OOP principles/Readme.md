Describe and explain how you used a range of OOP principles in your project. For each principle, include a very small code snippet that highlights the principle.
- Classes
    Classes allow for you to have instructions on how to create certain objects you can also have methods within a class to make the objects perform tasks. I used classes in my         code to describe and create people and shifts so employers can create rosters for their employees and the classes allowed me to easily create a lot of employees and shifts as       buninesses may need to create hundreds of employees and  simple set of instructions makes it a lot easier to code
```
  class Object:
    def __init__(self, name):
    def __init__(self, name: str):
        self._name = name
```
- Constructors
    Constructors are methods which get called whenever you create an instance of a class. I used it to assign attributes to employee objects when the intially get created.
    ```
        def __init__(self, name, contact_info, hours_worked, pay_rate, qualifications = []):
        super().__init__(name, contact_info)
        self.hours_worked = hours_worked
        self.pay_rate = pay_rate
        self.qualifications = qualifications
    ```
- Methods
    A method is a form of subprogram which only applies to a certain class. I use it in my code to set and get values for attributes which objects carry.
  ```
      @property
    def hours_worked(self):
        return self.hours_worked
  ```
- Objects
      Objects are instances of classes and they carry the information which the class determines. i use objects for all my employees and shifts as they require certain data to be         effective
- Inheritance
  
- Polymorphism
- Generalisation
