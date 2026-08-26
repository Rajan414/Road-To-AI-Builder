# part 3
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
# converted 

from dataclasses import dataclass
@dataclass
class student:
    name : str
    age : int
    marks : list
    
student = student("dai",28, [80,90,20])
print (student)
# right form

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    marks: list

student = Student("dai", 20, [80, 90, 20])

print(student)