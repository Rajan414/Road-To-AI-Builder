students = [
    {"name": "Dai", "marks": 85},
    {"name": "Rajan", "marks": 92},
    {"name": "Gyan", "marks": 78}
]
sorted_names = sorted(
    students, key=lambda student:student["marks"],
    reverse= True
)
print(sorted_names)
