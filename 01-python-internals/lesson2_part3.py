# this is for checking whether the address of the saved is same or different.

a = 10 
b = a
print(id(a))
print(id(b))
# # now for checking the output and reasining
a = [1,2]
b = a
b.append(3)

# print(a)
#  my theory: im sure that the output will be [1,2]
# because the values in a are also for b but
# when we append in b rather than in a then
# the append will occur in b values not in a 
# since the b now will have different values
# compare to a, so before a and b point to 
# single address box now after append , b
# will make another box. haha but it is wrong though true answer is 123

a = [1,2]
b = a
print (id(a))
print (id(b))

b.append(3)

print (id(a))
print (id(b))

print(a)
print(b)

# now this is another code
a = [1,2]
b = a
print ("before")
print("a:",a, id(a))
print("b:",b, id(b))

print ("append")
b.append(3)
print("a:",a, id(a))
print("b:",b, id(b))

print("\n Reset")
a = [1,2]
b = a

print("before +")
print("a:",a, id(a))
print("b:",b, id(b))

b = b + [3]

print ("\n After +")
print("a:",a, id(a))
print("b:",b, id(b))

