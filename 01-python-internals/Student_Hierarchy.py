# Dai | School Student | Average: 85.00
# Rajan | College Student | Average: 80.00
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def calculate_average(self):
        return sum(self.marks)/len(self.marks)
    
    def get_type(self):
        return"general student"
    
class SchoolStudent(student):
    def __init__(self, name, marks,school):
        super().__init__(name, marks)
        self.school = school
        
    def get_type(self):
        return"school student"
    
class CollegeStudent(student):
    def __init__(self, name, marks,college):
        super().__init__(name, marks)
        self.college = college
    def get_type(self):
        return "college student"

school_student = SchoolStudent(
    "Dai",
    [90, 85, 80],
    "ABC School"
)

college_student = CollegeStudent(
    "Rajan",
    [75, 80, 85],
    "XYZ College"
)

students = [school_student, college_student]
for student in students:
    print(f"{student.name} | {student.get_type()} | average = {student.calculate_average()}")