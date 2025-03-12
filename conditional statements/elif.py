country = input("Enter country name: ").lower()  
province = input("Enter province name: ").lower()  

if country == 'canada':  
    #nested if
    if province in ('alberta', 'nunavut', 'yukon'): #can also use [or]  
        tax = 0.05  
    elif province == 'ontario':  #else if
        tax = 0.10  
    else:  
        tax = 0.15  
else:  
    tax = 0.0  

print(f"Tax is {tax * 100}%")  
