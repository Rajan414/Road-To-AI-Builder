# practice
# Requirements:
# Receive the dictionary.
# Return a list of expense names.
# Only include expenses costing 500 or more.
# Use a list comprehension.
# Don't print inside the function.

def get_large_expenses(expenses):
    v = [name for name, values in expenses.items() if values >=500]
    return v

n = int(input("how many expenses u want to put?:"))
expenses ={}

for i in range(n):
    name = input ("enter the expense name:\n")
    print("----------------------------------------")
    amount = int(input("enter the expenses amount: "))
    print ("__________________________________________")
    expenses[name]= amount
    
print ("my expenses are :\n",expenses)
result = get_large_expenses(expenses)

print ("the expenses that are below or greater than 5000 are:\n")
print (result)


