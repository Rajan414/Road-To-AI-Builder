students = [
    {"id": 101, "name": "Dai"},
    {"id": 102, "name": "Rajan"},
    {"id": 103, "name": "Gyan"},
    {"id": 104, "name": "Sajan"}
]
studentss = {
    101: {"name": "Dai"},
    102: {"name": "Rajan"},
    103: {"name": "Gyan"},
    104: {"name": "Sajan"}
}
def find_student1(students, target_id):
    for student in students:
        if student["id"] == target_id:
            return student
    return None
def find_student(studentss, target_id):
    if target_id in studentss:
        return studentss.get(target_id)
    else:
        return None
print("---------------for linear search---------------")
print(find_student1(students,101))
print(find_student1(students,999))
print("---------------for binary search---------------")
print(find_student(studentss, 101))
print(find_student(studentss, 999))