
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import subprocess
import shlex

N = 10000
t0 = 100
dt = 2*t0/N

T = np.linspace(-t0, t0, N)
W = np.linspace(-100, 100, 200)

def rect_scalar(t):
    if np.abs(t) > 0.5:
        return 0
    else:
        return 1
    
rect = sp.vectorize(rect_scalar)

xt = np.sinc(T)
Xf = np.fft.fft(xt)
w = np.fft.fftfreq(len(xt)) * 2 * np.pi / dt
Xf *= dt * np.exp(1j * w * t0) / np.sqrt(2 * np.pi)
Xf /= Xf[0]

plt.plot(w, np.abs(Xf), label='Simulation')
#plt.plot(w, rect(w), label='Theoretical')
plt.gca().set_xlim(-10, 10)
plt.grid()
plt.title('Fourier Transform of $\mathrm{sinc}(t)$')
plt.xticks(color='w')
plt.legend()
plt.show()
#plt.savefig('../figs/3.10.png')
