# project
from dataclasses import dataclass,field

class InvalidAgeError(Exception):
    pass

@dataclass
class Student:
    name: str
    marks: list[int] = field(default_factory=list)
    _age: int = 0
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        if  0 <= value <= 120:
            self._age = value
        else:
            raise InvalidAgeError ("Invalid age")
        
    def __len__(self):
        return len(self.marks)   
    
    def calculate_average(self):
        return sum(self.marks)/len(self.marks)
    def __str__(self):
        return f"{self.name} => {self.marks} | {self.age}"

student = Student("Dai", [90, 85, 80], 20)
print(student)
print(len(student))
print(student.calculate_average())

try:
    student.age = 150
except InvalidAgeError as e:
    print(e)
student.age = 25
print(student.age)