#a = 20 #global
#print((id(a)))
#print((id(a)))
#def sample():
 #   a = 10 #local
  #  print(f"val of a is {a}")
   # def in_func():
    #    print(f"val of inner a is {a}")
    #in_func()
#sample()

b= 5
def operation():
    global b
    while b>0:
        print(b)
        b -= 1
operation()


