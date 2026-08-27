# Store the age internally as _age
# Create an @property called age
# Create an @age.setter
# Only allow ages from 0 to 120
# Invalid ages should print:invalid age
class student:
    def __init__(self,age):
        self._age = age
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        if 0< value < 120:
            self._age = value
        else:
            print("Invalid age")
        
student1 = student(20)

print(student1.age)

student1.age = 25
print(student1.age)

student1.age = 150
print(student1.age)