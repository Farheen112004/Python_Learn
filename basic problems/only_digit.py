s = input("Enter a string: ")

if s.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")


#without keyword
s = input("Enter a string: ")
only_digits = True

for ch in s:
    if ch < '0' or ch > '9':
        only_digits = False
        break

if only_digits:
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
