print ("----------------------------")

total = 0
count =0
def avg_marks( marks):
    total = 0
    count =0
    for i in marks:
        if i >= 50:
          total = total + i
          count = count +1
    avg = total / count
    return total, count, avg
total, count, avg = avg_marks([45, 72, 88, 31, 95, 64])
print ("total : ",total)
print ("passing : ",count)
print ("average : ",avg)
 
#  from previous
print ("0000000000000000000")
total = 0
count =0
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