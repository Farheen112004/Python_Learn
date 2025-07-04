arr = list(map(int,input().split()))
for i in range(len(arr)):
    profit = (max(arr) - min(arr))
    print (profit)
    break