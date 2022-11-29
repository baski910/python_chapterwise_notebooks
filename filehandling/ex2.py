###############################################################
# decorator is a technique for improving feature of a function
# without modifying code inside it
################################################################

def display(name):
    return f"welcome {name} to python"

print(display('bob')) # output will be 'welcome bob to python'

# <s>welcome bob to python</s>

def s_decorator(function_ref):
    def inner_wrapper(name):
        return "<s>{}</s>".format(function_ref(name))
    return inner_wrapper

#mydisplay = s_decorator(display)
display = s_decorator(display)
#print(mydisplay('bob'))
print(display('bob'))