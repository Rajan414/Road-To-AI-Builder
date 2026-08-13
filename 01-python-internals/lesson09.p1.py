# challenge 1
# Write a function:

# get_passing_students(students)

# It should:

# receive the list of dictionaries
# find students with marks >= 50
# return a list containing their names
# use a list comprehension
# don't print inside the function
# students = [
#     {"name": "Dai", "marks": 85},
#     {"name": "Ram", "marks": 42},
#     {"name": "Sam", "marks": 91},
#     {"name": "Alex", "marks": 37},
#     {"name": "Maya", "marks": 76}
# ]
def get_passing_students(students):
    x = [student["name"] for student in students if student["mark"] >= 50]
    return x
students = []
n = int(input("enter the list of dictionaries:"))
for i in range(n):
    student={}
    name = input("enter the name : ")
    mark = int(input("enter the mark: "))
    student["name"] = name
    student["mark"] = mark
    students.append(student)
    
    
result = get_passing_students(students)
print (result)

    