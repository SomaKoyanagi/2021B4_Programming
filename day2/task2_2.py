import numpy as np
import math

def relu(x):
    return np.maximum(0,x)

x = np.array([-1.0, 0.0, 0.5, 2.0])
print(relu(x))