# part 5 else
def safe_division():
    try:
        a= int(input("enter first num:"))
        b= int(input("enter sec num:"))
        c = a/b
        
    except ValueError:
        print("input number bro..")
    except ZeroDivisionError:
        print("u are putting zero bro..")
    else: 
        print (" nice bro u did perfectly")
        
    finally:
        print("u did great!")
result = safe_division()
print (result)