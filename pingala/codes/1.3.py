import numpy as np
import matplotlib.pyplot as plt
n = 100
alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2
k = np.linspace(1, n, n)
a = (alpha**k - beta**k)/(alpha - beta)
b = a[2:] + a[:98]
b = np.pad(b, (1, 0), 'constant', constant_values=(1, 0))
b_new = alpha**k + beta**k
if (np.allclose(b, b_new[:99])): print("verified")
else: print("incorrect")
#print(k)
#print(b)
plt.subplot(211)
plt.plot(k[1:],b,label=r'$b_{n}', color= 'r')
plt.grid()
plt.legend()
plt.subplot(212)
plt.plot(k,b_new,label=r'$\alpha^n+\beta^n$')
plt.grid()
plt.legend()
plt.show()
t = 10**k
tb = b*(1/t[:99])
eps = 1e-6
ans = 8/89
sb = np.cumsum(tb)
if (abs(sb[-1] - ans) < eps): print("1.4 verified")
else: print("1.4 incorrect")
plt.plot(k[1:],sb,label=r'$\sum_{k=1}^{n}\frac{b_{k}}{10^k}-8/89$')
plt.legend()
plt.grid()
plt.show()

