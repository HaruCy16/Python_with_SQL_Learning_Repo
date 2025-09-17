# Inheritance: reuse a base class

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

# Student inherits from Person
class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}")

student1 = Student("Alice", "Computer Science")
student1.greet()
student1.study()
