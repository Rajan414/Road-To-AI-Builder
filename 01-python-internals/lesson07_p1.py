# list comprehension
# Rules
# Use a list comprehension.
# Don't use a normal for loop.
# Don't use filter().
# Write the code yourself.
# Create a new list called passing_marks containing only marks >= 50.

# Expected result:

# [72, 88, 95, 64, 76]

marks = [45, 72, 88, 31, 95, 64, 28, 76]
passing_marks =[]
passing_marks = [mark for mark in marks if mark >= 50]
print (passing_marks)
#  another one 
numbers = [3, 8, 12, 15, 20, 25, 30, 41, 50]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
# another one
# doubled

# that contains every number multiplied by 2.
print("------------")
bingo = [2, 4, 6, 8, 10]
bingo_numbers= [x*2 for x in bingo]
print(bingo_numbers)
# new
# The store is having a 10% discount, but only on products costing ₹100 or more.
# Create a new list called:
# discounted_prices
# Expected result:
# [108.0, 180.0, 135.0]
# Requirements
# Use a list comprehension
# Only prices >= 100 receive the discount
# Discount = 10%
# Don't modify the original prices list
# Don't use a normal for loop
print("----prices----")
prices = [50, 120, 75, 200, 30, 150]
discounted_prices =[(x-((10/100)*x)) for x in prices if x >=100]
print(discounted_prices)
# next
# with these rules:
# Keep only numbers greater than 20
# From those, keep only even numbers
# Multiply each remaining number by 3
minor = [3, 10, 15, 22, 27, 30, 41, 50]
result = [x*3 for x in minor if x >20 and x%2==0 ]
print (result)