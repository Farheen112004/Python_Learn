# n = 5
# m = 0
# try:
#     ans = n/m
#     print(ans)
# except ZeroDivisionError as e: # or Exception
#     print("number cannot be printed")
# else:
#     print("no expception occured")
# finally:
#     print("running always")



# def func():
#     try:
#         raise ValueError("Initial")
#     finally:
#         raise RuntimeError("Cleanup")
# try:
#     func()
# except Exception as e:
#     print(e)



# def f():
#     try:
#         return "from try"
#     finally:
#         1/0
# print(f())


# try:
#      d = {}
#      v = d['key']
# except KeyError:
#     try:
#         v = 1/0
#     except ZeroDivisionError:
#         pass
# print("Done")

# def g():
#     try:
#         raise ValueError
#     except ValueError:
#         return "except"
#     finally:
#         return "finally"
# print(g())

# x =5
# print(1<x<5)



# if 6%3 or 5%3 
# print("passes")
# else:

# x = [1,2]
# print(id(x))
# y = x
# x +=[3]
# print(id(x))
# print(x,y,x is y)
