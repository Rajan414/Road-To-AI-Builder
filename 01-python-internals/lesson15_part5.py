# __init__()
# add_mark()
# remove_mark()
# calculate_average()
# __str__()
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def add_mark(self,mark):
        if 0 <= mark <=100: 
          self.marks.append(mark)
        else:
            print("invalid number..")
    def remove_mark(self,mark):
        self.marks.remove(mark)
    def calculate_average(self):
        return sum(self.marks)/len(self.marks)
    def __str__(self):
        return f"{self.name} => {self.marks} | avg: {self.name} => {self.calculate_average()}"
        
student = student("dai",[40,50,60,70])
student.add_mark(90)
student.add_mark(150)
student.add_mark(-5)
student.calculate_average()
print(student)