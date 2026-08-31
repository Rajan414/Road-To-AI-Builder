# 

def recursive_sum(numbers):
    if numbers ==[]:
        return 0
    return numbers[0] +(recursive_sum(numbers[1:]))
print(recursive_sum([2, 4, 6, 8]))