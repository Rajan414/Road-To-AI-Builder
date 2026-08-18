# json file creation
import json
students = [
    {"name": "Dai", "marks": [90, 85, 78]},
    {"name": "Ram", "marks": [75, 80, 88]}
]
with open("student.json","w") as file:
    json.dump(students, file)
    
with open("student.json","r") as file:
    data1 = json.load(file)
for student in data1:
    print (f"{student['name']} =>  {student['marks']}")