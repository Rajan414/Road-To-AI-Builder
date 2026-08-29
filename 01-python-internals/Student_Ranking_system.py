# ok lets do it
students = [
    {"name": "Dai", "marks": 85},
    {"name": "Rajan", "marks": 92},
    {"name": "Gyan", "marks": 78},
    {"name": "Sajan", "marks": 88}
]
ranked_students = sorted(
    students,
    key=lambda student : student["marks"],
    reverse= True)

top_student = ranked_students[0]
marks = [student["marks"] for student in students]
def student_average(marks):
    return sum(marks)/len(marks)

for count, student in enumerate(ranked_students, start=1):
    print(f"{count}. {student['name']} => {student['marks']}")
    
print(f"Top Student: {top_student['name']} => {top_student['marks']}")
print (f"Class Average: {student_average(marks):.2f}")