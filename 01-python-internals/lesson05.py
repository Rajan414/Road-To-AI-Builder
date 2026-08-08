# for loops

numbers = [3, 7, 10, 12, 15, 20]

for x in numbers:
    if x % 2 != 0:
        print(x)
        
# new loop
        
numbers = [2, 5, 8, 11, 14, 17]

total = 0

for x in numbers:
    if x % 2 == 0:
        total = total + x

print(total)    
# Start → total = 0  x = 2 → total = 2  x = 5 → total = 2  x = 8 → total = 10     x = 11 → total = 10     x = 14 → total = 24   x = 17 → total = 24  

   
# try new loop
marks = [45, 72, 88, 31, 95, 64]

total = 0
count = 0

for mark in marks:
    if mark >= 50:
        total = total + mark
        count = count + 1

print(total)
print(count)
# Start: total = 0 count = 0  mark = 45: total = 0 count = 0  mark = 72: total = 72 count = 1 ....mark = 88: total = 160 count = 2.....mark = 31: total = 160 count = 2...mark = 95: total = 255 count = 3 mark = 64: total = 319  count = 4  haha

# It should return two values:

# Total of marks ≥ 50
# Count of marks ≥ 50
print ("0000000000000000000")


def avg_marks( marks):
    total = 0
    count =0
    for i in marks:
        if i >= 50:
          total = total + i
          count = count +1
    # t = total
    
    # c = count
    avg = total / count
    return total, count, avg

    # print ("total : ",total)
    # print ("passing : ",count)
    # print ("average : ",avg)
    
    # print (avg)
    # print (t)
    # print (c)
total, count, avg = avg_marks([45, 72, 88, 31, 95, 64])
print ("total : ",total)
print ("passing : ",count)
print ("average : ",avg)
# modification 
print ("----------------------------")


def avg_marks( marks):
    total = 0
    count =0
    for i in marks:
        if i >= 50:
          total = total + i
          count = count +1
    # t = total
    
    # c = count
    avg = total / count
    # return total, count, avg

    print ("total : ",total)
    print ("passing : ",count)
    print ("average : ",avg)
    
    # print (avg)
    # print (t)
    # print (c)
result = avg_marks([45, 72, 88, 31, 95, 64])
 