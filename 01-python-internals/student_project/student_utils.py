# from storage import calculate_average
def calculate_average(marks):
     a= sum(marks)/len(marks)
     return a
 
def show_students(students):
    for student in students:
        st = calculate_average(student["marks"])
        print(f"{student['name']} => {st:.2f}")
    