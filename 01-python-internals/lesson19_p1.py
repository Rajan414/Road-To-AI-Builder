# Student_Search_System part
students = {
    101: {"name": "Dai"},
    102: {"name": "Rajan"},
    103: {"name": "Gyan"},
    104: {"name": "Sajan"}
}
def find_student(students, target_id):
    if target_id in students:
        return students.get(target_id)
    else:
        return None
print(find_student(students,101))
print(find_student(students,999))
