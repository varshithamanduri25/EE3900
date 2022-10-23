import matplotlib.pyplot as plt

x=[1,1]
y=[0]
for i in range(20):
  x.append(x[-1]+x[-2])
for i in range(1,20):
  y.append(x[i-1]+x[i+1])
plt.stem(range(20), y)
plt.grid()
plt.xlabel('[n]')
plt.ylabel('y[n]')
plt.tight_layout()
plt.show()
