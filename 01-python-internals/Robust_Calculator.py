# hehe
# project
def robust_calculator():
    try:
        a= int(input("enter first num:"))
        b= int(input("enter sec num:"))
        c = input("enter the operation(+, *, /, -): ")
        if c in ["+","*","/","-"]:
               if c== "+":
                   p = a+b    
               elif c=="*"  :
                   p= a*b
               elif c == "/":
                   p = a/b
               elif c == "-":
                   p = a-b
        else: 
             raise TypeError("u run into wrong op")
            
    except ValueError:
        print("input number bro..")
        
    except ZeroDivisionError:
        print("u are putting zero bro..")
        
    except TypeError:
        print("wrong operation")
        
    else: 
        print (f"{c} : answer: {p}")
        
    finally:
        print("u did great!")
result = robust_calculator()
print (result)