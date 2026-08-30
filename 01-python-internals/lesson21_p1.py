# new part
# left = 0
# right = len(numbers) - 1
# a while loop
# move left or right depending on the sum
# return True if found, otherwise False


def has_pair_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1
     
    while left < right :
        sum = numbers[left]+ numbers[right]
        if sum == target:
            return True
        elif sum<target:
            left += 1
        else:
            right -= 1
    return False
print(has_pair_sorted([2, 3, 5, 6, 8], 9))
    
        