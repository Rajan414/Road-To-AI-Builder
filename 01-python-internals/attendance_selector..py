# datetime part 2
# Your program should:

# Have a list of student names.
# Randomly select one student.
# Get the current date.
# Print something like:
import random 
import datetime
name = ["dai","vai","sai","aai","mai"]
mak = random.choice(name)
date1 = datetime.datetime.now()
date1.day
date1.month
date1.year
print(f"todays selected student: {mak}")
print(f"Date: {date1.year}-{date1.month}-{date1.day}")

