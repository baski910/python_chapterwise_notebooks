from math import exp

def activate(weights,inputs):
    activation = weights[-1] # bias
    for i in range(len(weights)-1):
        activation += weights[1]*inputs[i]
    return activation
