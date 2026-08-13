# part 2
# Rules
# Use a nested for loop.
# Don't use list comprehension.
# Don't use sum() yet.
# The function should print the marks.

# You already know everything required.
def print_all_marks(students):
    for student in students:
        for mar in student["marks"]:
            print (mar)
            
    
n = int(input("enter the times u want to create a dict: "))
students = []
for i in range (n):
    student = {}
    marks = []
    
    name = input("enter name: ")
    for j in range(3):
        mark = int(input ("enter marks: "))
        marks.append(mark)
    student["name"] = name
    student["marks"] = marks
    students.append(student)
print_all_marks(students)

