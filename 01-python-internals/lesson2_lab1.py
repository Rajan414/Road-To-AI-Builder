a = 10
b= 30
c= a+b
print (c)

# # 1. the role of a interpreter is to convert the given 
# code or any other data instruction to machine
# understandable language. 
# 2. python tokenizer is used because code need to be in
# understandable format since the code cannot understand
# directly by the system.
# 3.Parser check whether the code make sense or not .
# AST is build in python for taking right to left path
# which can help in solving the syntax logic in right order.
# AST for x=4+6:
    #   assignment
    #      |
    #      x
    # _____|______
    # | addition |
    # 4          6
           