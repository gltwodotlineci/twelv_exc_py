class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Mr/Miss {self.name} is {self.age} years old!")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    
    def display_details(self):
        super().display_details()
        print(f"And his monthly salary is {self.salary} euros")

print(">>>>> Person part <<<<<<")
person = Person("Aqif", 33)
person.display_details()
print("_______________")
print(">>>>> Employ part <<<<<<")
emp = Employee("Aqif", 22, 3000)
emp.display_details()
