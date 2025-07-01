def first_non_repeating(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return "No non-repeating character"

# Input and call
text = input("Enter a string: ")
print("First non-repeating character:", first_non_repeating(text))



# without count:
def first_non_repeating(s):
    freq = {}

    # Count frequency of each character
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Find the first character with frequency 1
    for ch in s:
        if freq[ch] == 1:
            return ch

    return "No non-repeating character"

# Input and call
text = input("Enter a string: ")
print("First non-repeating character:", first_non_repeating(text))
