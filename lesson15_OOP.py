class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)
    
student = Student("Dai", [90, 85, 78])

print(student.calculate_average())