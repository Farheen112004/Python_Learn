def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        print("value is : ",x)
    inner()
outer()
# case 2
x = 10
def outer():
    global x
    x += 10
    print("value is : ",x)
outer()

#case 3
def outer():
    x = [10,20]
    def inner():
        nonlocal x
        x.append(30)
        print(x)
    inner()
outer()
#ex
x = 1 #global
def foo():
    x = 10#local
    def bar():
        nonlocal x# enclosing scope
        x = 100
    bar()
    print(x)
foo()

#ex2
#fact = 10
def test():
    #fact = 0
    def recur(n):
        global fact
        fact = n
        if n > 1: 
            recur(n-1)
    recur(5)
    print(fact)
test()
