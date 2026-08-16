from calculations import student_average, top_student_record
from validation import get_positive_integer, get_name


students = []

n = get_positive_integer("How many students? ")
m = get_positive_integer("How many subjects? ")


for i in range(n):
    student = {}
    marks = []

    name = get_name("Enter student name: ")

    for j in range(m):
        while True:
            try:
                mark = int(input("Enter mark: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Enter a valid mark.")

    student["name"] = name
    student["marks"] = marks

    students.append(student)


print("\nStudent averages:")

for student in students:
    average = student_average(student["marks"])
    print(f"{student['name']} => {average:.2f}")


top_name, top_average = top_student_record(students)

print("\nTop student:")
print(f"{top_name} => {top_average:.2f}")