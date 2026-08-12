# another problem solving
# Requirements:
# Accept a list of words.
# Keep only words whose length is greater than 4.
# Convert those words to uppercase.
# Return the resulting list.
# Use a list comprehension.
# ["ai", "python", "code", "machine", "model"]
def get_long_words(words):
    v = [word.upper() for word in words if len(word)>4]
    return v
result = get_long_words(["ai", "python", "code", "machine", "model"])
print(result)

