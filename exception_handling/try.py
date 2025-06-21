n = 5
m = 0
try:
    ans = n/m
    print(ans)
except ZeroDivisionError as e:
    print("number cannot be printed")
else:
    print("no expception occured")
finally:
    print("running always")