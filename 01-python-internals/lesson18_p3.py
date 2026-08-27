# # 
# 0 <= age <= 120 → print "Age accepted"
# Anything else → raise InvalidAgeError("Invalid age")
class InvalidAgeError(Exception):
    pass
def add_marks(marks):
    if not 0<=marks<=120:
        raise InvalidAgeError("invalid age")
    print("age accepted")
try:
    add_marks(80)
except InvalidAgeError as a:
    print(a)