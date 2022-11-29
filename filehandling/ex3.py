###############################################################
# decorator is a technique for improving feature of a function
# without modifying code inside it
################################################################
###############################################################
# decorator is a technique for improving feature of a function
# without modifying code inside it
################################################################

def div_decorator(function_ref):
    def inner_wrapper(name):
        return "<div>{}</div>".format(function_ref(name))
    return inner_wrapper


def s_decorator(function_ref):
    def inner_wrapper(name):
        return "<s>{}</s>".format(function_ref(name))
    return inner_wrapper

# Accept-Ranges - response header

@div_decorator
@s_decorator # display = s_decorator(display)
def display(name):
    return f"welcome {name} to python"

# <div><s>welcome bob to python</s></div>

print(display('bob')) # output will be '<s>welcome bob to python</s>'

