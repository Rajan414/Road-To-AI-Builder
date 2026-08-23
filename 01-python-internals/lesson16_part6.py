# General Student
# School Student
# College Student
class student:
    def get_type(self):
        return"general student"
class SchoolStudent(student):
    def get_type(self):
        return"school student"
class CollegeStudent(SchoolStudent):
    def get_type(self):
        return "college student"
students = [
    student(),
    SchoolStudent(),
    CollegeStudent()
]

for student in students:
    print(student.get_type())