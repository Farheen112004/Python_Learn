string = "python"
vowels = "aeiou"
count = 0
const=0
for char in string:
    if char in vowels :
        count += 1    
    else:
        const += 1
print ("vowel: ",count)
print("const: ",const)
        
