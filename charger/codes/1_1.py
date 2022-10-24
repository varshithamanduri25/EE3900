import numpy as np
from matplotlib import pyplot as plt

A = 12
f = 50
t = np.linspace(0, 2/f, 1000)
plt.plot(t, np.abs(A*np.sin(2*np.pi*f*t)))
plt.grid()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show
