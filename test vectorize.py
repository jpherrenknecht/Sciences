import numpy as np


A=np.array([2,5,7])

def fonction(val):
    if val<3:
        val=0
    else:
        val=2*val + 3
    return val

fonc= np.vectorize(fonction)
a=2
print(fonc(A))




