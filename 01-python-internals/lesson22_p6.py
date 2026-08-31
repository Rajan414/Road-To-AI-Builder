# empty list
#     ↓
# base case

# first element == target?
#     ↓
# add 1 + recursive call

# otherwise
#     ↓
# recursive call only
def count_value(numbers, target):
     if len(numbers)==0:
            return 0
     if numbers[0] == target:
         return 1 + count_value(numbers[1:],target)
     else:
         return count_value(numbers[1:],target)
print(count_value([2, 5, 2, 7, 2, 9], 2))
# [5, 10, 15, 20]

# 5 + recursive_sum([10, 15, 20])
def recursive_sum(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])
print(recursive_sum([5, 10, 15, 20]))\
  
  
def recursive_length(text):

    if text == "":
        return 0

    return 1 + recursive_length(text[1:])

print(recursive_length("python"))
