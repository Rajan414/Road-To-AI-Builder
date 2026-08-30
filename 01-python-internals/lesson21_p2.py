# Calculate the first window sum.
# Store it as max_sum.
# Slide through the rest of the list.
# Return the maximum window sum.

# Test it with:
def max_window_sum(numbers, window_size):
    window_sum = sum(numbers[:window_size])
    max_sum = window_sum
    for i in range (window_size , len(numbers)):
        window_sum = (window_sum - numbers[i - window_size] + numbers[i]
        )
        max_sum = max(max_sum, window_sum)
    return max_sum

print(max_window_sum([4, 2, 7, 3, 6], 2))