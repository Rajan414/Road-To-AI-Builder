# finally lesson 10
def safe_integer_input():
    while True:
        try: 
          n = int(input("enter a number: ")) 
          return n
        except: 
            print("enter numbers....bro ")
r = safe_integer_input()
print(r)
