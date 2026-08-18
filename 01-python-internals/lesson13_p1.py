# file handling
# Write a program that:

# Opens students.txt in read mode
# Reads all the lines
# Prints each student's name without the extra newline problem
# Hint
with open ("student.txt","w") as file:
    file.write("Dai\n")
    file.write("Ram\n")
    file.write("Sam\n")
with open("student.txt", "r")as file:
    file1 = file.readlines()
for line in file1:
    print(line.strip())
    
    
