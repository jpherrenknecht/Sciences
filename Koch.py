import numpy as np
import matplotlib.pylab as plt
def koch (a,b,n,alpha):
    m=(2.+2.*np.cos(alpha))
    R=np.array([[np.cos(alpha),-np.sin(alpha)],[np.sin(alpha),np.cos(alpha)]])
    if n==0:
        plt.plot([a[0],b[0]],  a[1],b[1],'k')

    else:
        c=a+(b-a)/m
        d=b-(b-a)/m
        e=c+np.dot(R,((d-c)/(2*np.cos(alpha))))

        koch(a,c,n_1,alpha)
        koch(c,e,n-1,alpha)
        koch(e, d, n - 1, alpha)
        koch(d, b, n - 1, alpha)