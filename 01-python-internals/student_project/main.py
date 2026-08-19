# main 
# import json
from storage import save_students, load_students
from student_utils import calculate_average, show_students
def main():
  students = load_students()
  
  student = create_student()
  students.append(student)
  save_students(students)
  
  show_students(students)

def create_student():
    name = input("Enter name: ")
    c = int(input ("enter the marks you want to put 3 to 4: "))
    marks = []
    
    for i in range(c):
        mark = int(input("Enter mark: "))
        marks.append(mark)

    return {
        "name": name,
        "marks": marks
    }
    
if __name__ == "__main__":
    main()