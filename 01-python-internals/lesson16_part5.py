# try
# inherit name and marks
# have an additional attribute called school
# use super() to initialize the parent attributes

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def calculate_average(self):
        return sum(self.marks)/len(self.marks)
        
class SchoolStudent(student):
    def __init__(self, name, marks,school):
        super().__init__(name, marks)
        self.school = school
        
student = SchoolStudent(
    "Dai",
    [90, 85, 80],
    "ABC School"
)

print(student.name)
print(student.marks)
print(student.school)
print(student.calculate_average())