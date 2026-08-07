# starting function 
def add():
    print (5+10)

add()
# output will be 15

def hello():
    print("Hello")

print("A")

hello()

print("B")

hello()
#  output will be A hello B hello
def add(a, b):
    print(a + b)

add(5, 10)
add(20, 30)
add(100, 200)

#  another one p1
def greet(name):
    print("Hello", name)

greet("Dai")

greet("OpenAI")

greet("Engineer")
# this one was bonus round question too ez
a = 100

def first():
    print(a)

def second():
    a = 50
    print(a)

print(a)

first()

second()

print(a)
# prediction pt 2
def add(a, b):
    return a + b

def multiply(x):
    return x * 2

answer = multiply(add(5, 10))

print(answer)
# this one is boss challenge lol haha
