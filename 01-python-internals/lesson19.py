# linear search

students = [
    {"id": 101, "name": "Dai"},
    {"id": 102, "name": "Rajan"},
    {"id": 103, "name": "Gyan"},
    {"id": 104, "name": "Sajan"}
]
def find_student(students, target_id):
    for student in students:
        if student["id"] == target_id:
            return student
    return None
       

print(find_student(students, 101))
print(find_student(students, 999))