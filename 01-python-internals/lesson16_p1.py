
class Student:
    def __init__(self, name):
        self.name = name


class CollegeStudent(Student):
    def __init__(self, name, college):
        self.college = college
student = CollegeStudent("Dai", "ABC College")

print(student.college)
print(student.name)