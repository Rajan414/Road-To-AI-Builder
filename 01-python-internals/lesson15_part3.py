class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def remove(self, mark):
        self.marks.remove(mark)


student = Student("dai", [90, 80])

student.remove(80)

print(student.marks)