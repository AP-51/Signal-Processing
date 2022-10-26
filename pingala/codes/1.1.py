import numpy as np
import matplotlib.pyplot as plt
n = 100
alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2
k = np.linspace(1, n, n)
a = (alpha**k - beta**k)/(alpha - beta)
ca = np.cumsum(a)
if (np.allclose(ca[:98], a[2:] - 1)): print("verified")
else: print("incorrect")
plt.subplot(211)
plt.plot(k,a,label=r'$\sum_{k=1}^{n}a_{k}$',color='r')
plt.grid()
plt.legend()
plt.subplot(212)
plt.plot(k,ca,label=r'$a_{n+2}-1')
plt.grid()
plt.legend()
plt.show()

