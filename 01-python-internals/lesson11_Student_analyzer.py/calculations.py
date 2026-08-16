def student_average(marks):
    total = 0

    for mark in marks:
        total = total + mark

    average = total / len(marks)
    return average


def top_student_record(students):
    highest = 0
    top = ""

    for student in students:
        average = student_average(student["marks"])

        if average > highest:
            highest = average
            top = student["name"]

    return top, highest