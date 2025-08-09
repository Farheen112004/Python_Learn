#Check if a 2D matrix is an identity matrix (1s on diagonal, 0s elsewhere).
matrix = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
    ]
rows = len(matrix)
cols = len(matrix[0])
is_identity = True
if rows != cols:
    is_identity = False
else:
    for i in range(rows):
        for j in range(cols):
            if i == j and matrix[i][j] != 1:
                is_identity = False
            elif i!=j and matrix[i][j] != 0:
                is_identity = False
                break
if is_identity:
    print("its identity bro")
else:
    print("nope")