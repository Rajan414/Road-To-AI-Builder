# project = Student Management design
# Dai | School Student | Average: 85.00
# Rajan | College Student | Average: 80.00

from abc import ABC,abstractmethod

# class student(abc):
#     name:str
#     marks:list
#     school: str
#     college: str
# @abs
    
class student(ABC):
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    def calculate_average(self) -> float:
        return sum(self.marks)/len(self.marks)
    
    @abstractmethod
    def gettype(self):
        pass
    
class school_student(student):
    def __init__(self, name, marks,school):
        super().__init__(name, marks)
        self.school = school
        
    def gettype(self):
        return "school student"
    
class college_student(student):
    def __init__(self, name, marks,college):
        super().__init__(name, marks)
        self.college = college
        
    def gettype(self):
        return "college student"
    
school = school_student(
    "Dai",
    [90, 85, 80],
    "ABC School"
)

college = college_student(
    "Rajan",
    [75, 80, 85],
    "XYZ College"
)
students = [school,college]

for student in students:
    print(
        f"name : {student.name} |"
        f"{student.gettype()}|"
        f"average: {student.calculate_average():.2f}"
    )