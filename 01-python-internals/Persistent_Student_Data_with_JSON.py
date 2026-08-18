# # project work
# import json

# students = []
# def student_asking(prompt):
#     try:
#         valid = int(input(prompt))
#         # valid1 = int(input(prompt))
#         if valid :
#             return valid
#     except:
#         print ("enter valid input bro...")
    
# n = student_asking("how much do you want to put dictionary: ")
# m = student_asking("how much value do you want to put: ")
# for i in range (n):
#     student = {}
#     marks = []
#     name  = input("enter the name: ")
#     for j in range(m):
#         mark = int(input("enter the marks:"))
#         marks.append(mark)
#     student["name"] = name
#     student["marks"] = marks
#     students.append(student)
# def jsonfunction(hello):
#     try:
#      with open("students.json", "w") as file:
#         json.dump(students, file)

#      with open("students.json", "r") as file:
#         data = json.load(file)
#      if students.json :
#          return data
#     except FileNotFoundError:
#         print("lol file not found create it bro..")
# result = jsonfunction(students)
# for st in result:
#     print(f"{st['name']} => {st['marks']}") 
# new version


import json

students = []

try:
    with open("students.json", "r") as file:
        students = json.load(file)

except FileNotFoundError:
    print("No saved students yet.")
    
# with open("students.json","r") as file:
#     data = json.load(file)
def student_asking(prompt):
    try:
        valid = int(input(prompt))
        # valid1 = int(input(prompt))
        if valid :
            return valid
    except:
        print ("enter valid input bro...")
    
n = student_asking("how much do you want to put dictionary: ")
m = student_asking("how much value do you want to put: ")
for i in range (n):
    student = {}
    marks = []
    name  = input("enter the name: ")
    for j in range(m):
        mark = int(input("enter the marks:"))
        marks.append(mark)
    student["name"] = name
    student["marks"] = marks
    students.append(student)
    
with open("students.json", "w") as file:
     json.dump(students, file)

def student_average(marks):
    total = 0

    for mark in marks:
        total += mark

    return total / len(marks)

with open("students.json", "r") as file:
    students = json.load(file)
    
for student in students:
    average = student_average(student["marks"])
    print("_______________output___________________--")
    print(f"{student['name']} => {average:.2f}")