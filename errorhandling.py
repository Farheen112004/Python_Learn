x = 42
y = 0
print()
try: 
    print (x/y)   
except ZeroDivisionError as e:
    print('not allowed to be divided by zero')
else:
    print('something went wrong')
finally:
    print('this will always be printed cleanup code')

