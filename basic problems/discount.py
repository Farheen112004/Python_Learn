r1 = int(input())
r2 = int(input())
r3 = int(input())

total = r1 + r2 + r3

discount = 0.8 * total  #disc = (total - (20*total // 100))
free_item = total - min(r1, r2, r3)

if discount < free_item:
    print("DISCOUNT")
else:
    print("FREE ITEM")
