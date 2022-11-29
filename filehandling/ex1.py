####################################################
# nested function - function inside a function
# closure - returns the reference of inner function
#           
#####################################################

def f(x):
    #def g(y):
    def g():
        return x*x
        #return y*y
    #return x+g(x)
    return g

g = f(10)

print(g)

print(g())