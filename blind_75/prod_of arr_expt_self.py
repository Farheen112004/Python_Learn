arr = list(map(int,input().split()))
res = []
for i in range(len(arr)):
    prod = 1
    for j in range(len(arr)):
        if i != j:
            prod *= arr[j]
    res.append(prod)
print(res)
        