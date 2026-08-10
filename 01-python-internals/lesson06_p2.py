# sets 
python_students = {"Dai", "Ram", "Sam", "Alex"}
ml_students = {"Dai", "Alex", "John"}

print(python_students & ml_students)
unique_sets = set (python_students)
print(len(unique_sets))
print("Dai" in python_students)

students = {"Dai", "Ram", "Sam"}

students.add("Alex")
students.add("Dai")

print(students)
