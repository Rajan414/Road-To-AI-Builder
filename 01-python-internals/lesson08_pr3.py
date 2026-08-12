# harder question
# combine functions + dictionaries + comprehensions.

# It should:

# receive the dictionary
# return a list of names
# only include students with scores >= 80
# use a list comprehension
# don't print inside the function

def get_top_students(students):
    b = [name for name,values in students.items() if values>=80]
    return b
result = get_top_students(students = {
    "Dai": 85,
    "Ram": 42,
    "Sam": 91,
    "Alex": 37,
    "John": 76,
    "Maya": 88
})
print (result)


    