n = int(input("Enter number: "))

# Top part: both triangles grow
for i in range(1, n + 1):
    # Left triangle
    for j in range(i):
        print("*", end=" ")
    
    # Spaces in between
    for j in range((n - i) * 4):
        print(" ", end="")
    
    # Right triangle
    for j in range(i):
        print("*", end=" ")
    
    print()  # move to next line

# Bottom part: both triangles shrink
for i in range(n - 1, 0, -1):
    # Left triangle
    for j in range(i):
        print("*", end=" ")
    
    # Spaces in between
    for j in range((n - i) * 4):
        print(" ", end="")
    
    # Right triangle
    for j in range(i):
        print("*", end=" ")
    
    print()  # move to next line
