# final try
# Create a list called:
# top_students
# containing the names of students who scored 80 or higher.
# Expected names, in dictionary iteration order:
# ["Dai", "Sam", "Maya"]
# Requirements
# Use a list comprehension
# Use the dictionary
# Don't use a normal for loop
# Don't use filter()
students = {
    "Dai": 85,
    "Ram": 42,
    "Sam": 91,
    "Alex": 37,
    "John": 76,
    "Maya": 88
}
top_students =[name for name,values in students.items() if values>=80]
print (top_students)
print("_______________________")
# new assignment
# Create a list called long_words containing only words whose
# length is greater than 4, but store the words in uppercase.

# For example, "python" should become "PYTHON".
words = ["python", "ai", "machine", "learning", "code", "model"]
long_words= [ word.upper() for word in words if len(word)>4]
print(long_words)
# for x in words:
#  long_words= []
#  if len(words)>4:
#      long_words.append(x)
# print (long_wordss)