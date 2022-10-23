import matplotlib.pyplot as plt

x=[1,1]
for i in range(20):
  x.append(x[-1]+x[-2])
plt.stem(range(len(x)), x)
plt.grid()
plt.xlabel('[n]')
plt.ylabel('x[n]')
plt.tight_layout()
plt.show()
