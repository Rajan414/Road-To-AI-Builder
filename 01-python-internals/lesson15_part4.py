# class
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def add_marks(self, mark):
        self.marks.append(mark)
    def __str__(self):
        return f"{self.name} => {self.marks}"
student = student("dai",[90,80,100])
student.add_marks(200)
print(student)