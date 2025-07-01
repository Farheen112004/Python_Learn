# Input string
s = input("Enter a string: ")

# Convert to character array (list of characters)
char_array = list(s)
print("Character array:", char_array)

# Convert back to string
new_string = ''.join(char_array)
print("Back to string:", new_string)
