import numpy as np


A=np.array([2,1,7])

def fonction(val):
    if val<3:
        val=0
    else:
        val=2*val + 5
    return val



fonc= np.vectorize(fonction)
a=
print(fonc(A))




