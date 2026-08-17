# project work
def top_student_record(students):
    highest = 0 
    top = ""
    for student in students:
        avgr = student_average(student["marks"])
        if avgr > highest:
            highest = avgr
            top = student["name"]
    return top, highest     
 
def student_average(marks):
        total = 0
        for mar in marks:
            total = total+ mar
        avg = total/len(marks)
        return avg

def student_data_avg(students):
    for student in students:
        v = student_average(student["marks"])
        print(f"{student['name']} => {v:.2f}")
    a,b = top_student_record(students)
    print(f"{a} => {b}")
   
n = int(input("how much dictionary u want to create: "))
m = int(input("how many subjects amount u want to put: "))
students = []
for i in range(n):
    student = {}
    marks = []
    name = input("enter the name: ")
    for j in range(m):
        mark = int(input("enter the mark:"))
        marks.append(mark)
        
    student["name"] = name
    student["marks"] = marks
    students.append(student)     
print (students)
pero = student_data_avg(students)
print (pero)