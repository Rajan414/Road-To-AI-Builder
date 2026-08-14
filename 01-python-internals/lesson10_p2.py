# part 2 haita

def safe_integer_input():
    while True:
        
        try: 
            
          age = int(input("enter your age: ")) 
          if age >0:
           return age
          else:
              print("enter positive numbers....bro ")
              
        except: 
            print("enter numbers....bro ")
        
r = safe_integer_input()
print(r)
