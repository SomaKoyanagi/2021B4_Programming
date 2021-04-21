import numpy as np
import math

def sigmoid(x):
    result = 1/(1+e**-x)
    return result

e = math.e
x = np.array([-1.0, 0.0, 0.5, 2.0])

print(sigmoid(x))
