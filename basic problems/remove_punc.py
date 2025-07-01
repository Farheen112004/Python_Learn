#remove all punctuations from string
s = input("enter string: ")
punc = ("!@#$%^&*")
new = ""
for char in s:
    if char not in punc:
        new += char
    
if new == s:
    print("no punctuation")
else:
    print("without punctuation: ",new)


#with function
#remove all punctuations from string
def func(string):
    punc = ("!@#$%^&*")
    new = ""
    for char in s:
        if char not in punc:
            new += char
    
    if new == s:
        print("no punctuation")
    else:
        print("without punctuation: ",new)
    
s = input("enter string: ")
func(s)