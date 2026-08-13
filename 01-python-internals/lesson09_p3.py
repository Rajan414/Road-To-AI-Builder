# new part for lesson 09 yep
# Accept a list of marks.
# Calculate the total using a for loop.
# Calculate the average.
# Return the average.
# result = calculate_average(marks = [85, 90, 78])
# print (result)
# next challenge
print("---------------------------------------------------")

def calculate_average(marks): 
    total = 0
    for mark in marks:
        total = total+ mark
    avg = total/len(marks)
    return avg

def print_student_averages(students):
    for student in students:
        v=calculate_average(student["marks"])
        print (f"{student["name"]} => {v:.2f}")
    
    
result = print_student_averages(students = [
    {"name": "Dai", "marks": [85, 90, 78]},
    {"name": "Ram", "marks": [42, 55, 48]},
    {"name": "Sam", "marks": [91, 95, 88]},
    {"name": "Maya", "marks": [76, 82, 80]}
])
print (result)
