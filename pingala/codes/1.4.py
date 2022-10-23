import numpy as np

alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2
n=50
b=[]
for i in range(n):
   b.append((alpha**i + beta**i)/10**i)   #taken from 1.3
sum=0
for i in range(n-1):
  sum=sum+b[i]
print(sum)
if (np.allclose(sum, 8/89)): 
  print("correct")
else: 
  print("incorrect")
