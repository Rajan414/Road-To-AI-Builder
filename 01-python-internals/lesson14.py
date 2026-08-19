# reusable and refactoring
# Write the save_students() function yourself.

# Requirements:

# Function name: save_students
# Takes students as an argument
# Opens students.json
# Uses write mode
# Saves using json.dump()
# Use indent=4
def save_students(students):
    with open("students.json","w") as file:
        json.dump(students, file, indent = 4)
    
def load_students():
    try: 
        with open("students.json","r")as file:
           return json.load(file)
    except FileNotFoundError:
        return []
    
def calculate_average(marks):
     a= sum(marks)/len(marks)
     return a
 
def show_students(students):
    for student in students:
        st = calculate_average(student["marks"])
        print(f"{student['name']} => {st:.2f}")
    