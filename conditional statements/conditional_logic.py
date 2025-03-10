price = int(input('enter the price: '))
print(price)
if price >= 30:  #money we have rn
    print("You can't buy the item.")
else:
    print("You can afford the item.")
print('\n')

#converting string to lower 'since python only has case sensitive comparison
name = 'FARHEEN'
if name.lower() == 'farheen':
    print('wassup Farr')
else:
    print('welpo whos this then?')