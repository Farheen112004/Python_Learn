s = input("Enter string: ")
new = ""
for char in s:
    if char.isupper():
        new += char.lower()
    elif char.islower():
        new += char.upper()
    else:
        new += char
        
print("string:",new)

