def rev(string):
    if len(string)<= 1 :
        return string
    mid = len(string) // 2
    left = string[:mid]
    right = string[mid:]
    return (rev(right) + rev (left))
s = input("enter string: ")
output = rev(s)
print("reveresed: ",output)
#divide and conquer