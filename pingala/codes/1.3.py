import numpy as np
import random
alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2
n=50
a=[]
for i in range(n):
   a.append((alpha**i - beta**i)/(alpha - beta))
k = random.randint(0,n)  #some random number
b = a[k-1]+a[k+1]
b_new = alpha**k + beta**k
if (np.allclose(b, b_new)): 
  print("correct")
else: 
  print("incorrect")
