# 2. Print all pairs (i, j) such that i + j = 10 where 1 <= i, j <= 9.
for i in range(1, 10):      
    for j in range(1, 10):   
        if i + j == 10:
            print(i, j)
