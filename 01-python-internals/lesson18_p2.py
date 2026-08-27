#
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def __len__(self):
        return len(self.marks)
    def __str__(self):
       return f"{self.name} => {self.marks}"
student1 = student("Dai", [90, 80, 70])

print(len(student1))
print(student1)