# student analysis
# It should:
# Accept a list of numbers.
# Find only the even numbers.
# Return the new list.
# Use a list comprehension inside the function.
def get_even_numbers(numbers):
    n = [x for x in numbers if x%2==0]
    return n
result = get_even_numbers([2,45,67,99,33,55,42,40])
print(result)


