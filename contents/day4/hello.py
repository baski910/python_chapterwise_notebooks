__all__=['addnum','divnum']
def addnum(a,b):
    return a+b

def divnum(a,b):
    return a/b

def sayHello():
    print("hello")

if __name__ == "__main__":
    print("called from module:",__name__) # __name__ is __main__ when executed as standalone script return the modulename when imported
    print("called from module:",addnum(30,3))
    print("called from module:",divnum(30,3))