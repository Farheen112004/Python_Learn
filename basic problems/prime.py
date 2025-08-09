for num in range(2,101):
    prime = True
    for i in range(2,int(num ** 0.5) + 1): # Check divisibility up to the square root of num
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)