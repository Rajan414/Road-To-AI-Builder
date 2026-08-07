a = 100
b = 100

print (id(a))
print (id(b))
print (a is b)


a = 1000
b = 1000

print (id(a))
print (id(b))
print (a is b)
print()
print()
print("-----------------")
a = 1000
b = int("1000")

print("a id:", id(a))
print("b id:", id(b))

print("a == b:", a == b)
print("a is b:", a is b)

print ("=====================================")
a = []
b = []

print(a == b)
print(a is b)

a.append(1)

print(a)
print(b)