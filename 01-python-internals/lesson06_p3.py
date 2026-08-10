# dictionary
student = {
    "name": "Dai",
    "age": 20
}

student["age"] = 21
student["city"] = "Kathmandu"

print(student)
# next
print("---------------")

marks = {
    "Dai": 85,
    "Ram": 42,
    "Sam": 91,
    "Alex": 37
}

for name in marks:
    if marks[name] >= 50:
        print(name)
        

# final boss challenge 
marks = {
    "Dai": 85,
    "Ram": 42,
    "Sam": 91,
    "Alex": 37,
    "John": 76
}

total = 0
count = 0

for name, score in marks.items():
    if score >= 50:
        total += score
        count += 1

print(total)
print(count)
# Start → total = 0 count = 0

# Dai   → total = 85 count = 1
# Ram   → total =85 count = 1
# Sam   → total = 176 count = 2
# Alex  → total = 176 count = 2
# John  → total = 252 count = 3
