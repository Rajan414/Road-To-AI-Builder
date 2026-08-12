# project 1
# The user should enter any number of expenses.
# Your program must:

# Ask how many expenses they want to enter.
# Collect expense name + amount.
# Store them in a dictionary.
# Create a function that returns the total amount spent.
# Create a function that returns the largest expense name and amount.
# Create a function that returns a list of expenses costing 500 or more.
# Print all three results.
# expense analyzer


def total_amount_spent(expense):
    total = 0
    for value in expense.values():
        total = total + value
    return total

def largest_expense(expense):
    largest = max(expense.values())
    for name, values in expense.items():
        if values == largest:
            return name,values
        
def get_large_expenses(expense):
    y = [name for name, values in expense.items() if values >=500]
    return y

expense={}

n = int(input("how many expenses u want to enter: "))
for i in range(n):
    name = input("enter the expense name: ")
    amount = int(input("enter the expense amount: "))
    expense[name] = amount
    
    
a = total_amount_spent(expense)
b = largest_expense(expense)
c = get_large_expenses(expense)
print (" total spent: ",a)
print(b)
print ("list of expenses above 500: ",c)

