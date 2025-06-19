n = int(input("enter num : "))
for i in range(n):
    for j in range(i,n):
        print("*", end = " ")
    print()


#other method
for i in reversed(range (n)):
    print("*" * i)
    n += 1