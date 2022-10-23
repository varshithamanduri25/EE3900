import numpy as np

alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2
n=50
a=[]
for i in range(n):
   a.append((alpha**i - beta**i)/(alpha - beta)/10**i)
sum=0
for i in range(n):
  sum=sum+a[i]
if (np.allclose(sum, 10/89)): 
  print("correct")
else: 
  print("incorrect")
