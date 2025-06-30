string = input("Enter your string: ")
longest =""
temp = ""
for char in string:
    if char in temp:
        temp = temp[temp.index(char)+1:] #removes duplicates
    temp += char
    if len(temp) > len(longest):
        longest = temp
print("longest substring: ", longest)
        