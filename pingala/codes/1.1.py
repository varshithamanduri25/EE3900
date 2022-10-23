import numpy as np

alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2
n=50
a=[]
for i in range(n):
   a.append((alpha**i - beta**i)/(alpha - beta))
sum=0
for i in range(n-2):
  sum=sum+a[i]
if (np.allclose(sum, a[n-1] - 1)): 
  print("correct")
else: 
  print("incorrect")
