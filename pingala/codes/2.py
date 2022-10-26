import numpy as np
import matplotlib.pyplot as plt
import scipy
def xn(n):
    if n<0:
        return 0
    if n==0 or n==1:
        return 1
    if n>1:
        return x(n-1)+x(n-2)
def yn(n):
    return xn(n-1)+xn(n+1)
n=np.arange(10)
x=scipy.vectorize(xn)
y=scipy.vectorize(yn)
#2.1
plt.stem(n,x(n))
plt.xlabel("n")
plt.ylabel("x(n)")
plt.grid()
plt.show()
#2.5
plt.stem(n,y(n))
plt.xlabel("n")
plt.ylabel("y(n)")
plt.grid()
plt.show()


