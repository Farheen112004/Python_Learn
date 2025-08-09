# 3. Find and print all Armstrong numbers between 1 and 500 using nested loops.
for num in range(1, 501):
    num_str = str(num)
    num_len = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit) ** num_len  # power of digits
    
    if total == num:
        print(num)
