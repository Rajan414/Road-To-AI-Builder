# final multiple handling
def safe_division():
    try:
        a = int(input("enter the first number:"))
        b = int(input("enter the sec number:"))
        c = a/b
        return c
    except ValueError:
        print ("invalid number..")
    except ZeroDivisionError: 
        
        print("being devide by zero..")
        
        
result = safe_division()
print(result)