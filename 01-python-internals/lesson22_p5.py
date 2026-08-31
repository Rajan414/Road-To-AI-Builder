def recursive_max(numbers):
    if len(numbers)==1:
        return numbers[0]
    rest_max = recursive_max(numbers[1:])
    if numbers[0]> rest_max:
        return numbers[0]
    else:
        return rest_max
print(recursive_max([3, 9, 2, 15, 7]))