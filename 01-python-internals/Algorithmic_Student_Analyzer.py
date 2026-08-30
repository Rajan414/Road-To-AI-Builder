def has_duplicate_ids(student_ids):
    seen = set()
    for student_id in student_ids:
        if student_id in seen:
            return True
        seen.add(student_id)
    return False

def has_mark_pair(marks, target):
    left = 0
    right = len(marks)-1
    while left< right:
        sum1 = marks[left] + marks [right]
        if sum1==target:
            return True
        elif sum1<target:
            left += 1
        else:
            right -=1
    return False
def max_consecutive_sum(scores, window_size):
    win_sum = sum(scores[:window_size])
    max_sum = win_sum
    for i in range( window_size, len(scores)):
        win_sum = (
            win_sum - scores[i-window_size] + scores[i]
        )
        max_sum = max (max_sum, win_sum)
    return max_sum

print(has_duplicate_ids( [101, 102, 103, 102, 105]))

print(has_mark_pair([60, 70, 75, 80, 90],145))

print (max_consecutive_sum([10, 20, 30, 15, 25, 40],2))
