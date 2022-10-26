import numpy as np
import matplotlib.pyplot as plt
n = 100
alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2
k = np.linspace(1, n, n)
#print(k)
a = (alpha**k - beta**k)/(alpha - beta)
t = 10**k
ta = a*(1/t)
eps = 1e-6
ans = 10/89
sa = np.cumsum(ta)
if (abs(sa[-1] - ans) < eps): print("verified")
else: print("incorrect")
#plt.subplot(211)
plt.plot(k,(sa-ans),label=r'$\sum_{k=1}^{n}\frac{a_{k}}{10^k}-(\frac{10}{89})$',color='g')
plt.legend()
plt.grid()
plt.show()
