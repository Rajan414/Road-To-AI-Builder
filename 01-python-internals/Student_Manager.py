# project 1 in OOP
# Put all three objects into a list called students.
# Add a new mark to one student using .add_mark().
# Remove a mark from another using .remove_mark().
# Loop through the students list.
# Print each student using:
# Dai
# Gyan
# Sajan
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def add_marks(self,mark):
        if 0<=mark<=100:
            self.marks.append(mark)
        else:
            print("invalid number")
            
    def remove_mark(self,mark):
        self.marks.remove(mark)
        
    def calculate_average(self):
        return sum(self.marks)/len(self.marks)
    
    def __str__(self):
        return f"{self.name} => {self.marks} \n avg: {self.name} => {self.calculate_average():.2f}"
s1= student("dai",[40,50,60])
s2= student("gyan",[56,50,98])
s3= student("sajan",[45,67,90])

students = [s1,s2,s3]

s1.remove_mark(50)
s2.add_marks(89)
for student in students:
   print(student)

