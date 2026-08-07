import dis
def add():
    x = 5
    y = 10
    return x+y
dis.dis(add)
# practice set 2
num = 1
for i in range (1,6):
    for j in range (i):
        print (num,end = " ")
        num = num+1
    print ()