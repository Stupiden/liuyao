class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def printName(self):
        print(self.firstname + " " + self.lastname)
    
class Student(Person):
    def __init__(self, firstname, lastname, area):
        super().__init__(firstname, lastname)
        self.area = area
    def printNameSubject(self):
        print(f"Student: {self.firstname} {self.lastname}, Area: {self.area}")
class Teacher(Person):
    def __init__(self, firstname, lastname, subject):
        super().__init__(firstname, lastname)
        self.subject = subject
    def printNameSubject(self):
        print(f"Teacher: {self.firstname} {self.lastname}, Subject: {self.subject}")