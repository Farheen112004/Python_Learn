arr = list(map(int,input().split()))
found = False
for i in range(len(arr)):
    for j in range(i + 1 , len(arr)):
        if arr[i] == arr[j]:
            found = True
            break
print(found)
    
        