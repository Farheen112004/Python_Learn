def second_largest(listuu=[5,1,4,3,8]):
    og_max = max(listuu) 
    listuu.remove(og_max)                  
    return max(listuu)                

print("Second largest:", second_largest())
