from random import *
# 1)

graine = 10

seed(graine)

# 2)

import numpy as np

arr = np.random.randn(500)

# 3)

alpha=15
muu=100

arr=arr*alpha+muu

# 4-7)

import matplotlib.pyplot as plt


bins=plt.hist(arr,50)
plt.ylabel("Probabilité de densité")
plt.xlabel("Quotient intellectuel")
plt.grid(True)
plt.show()

print(bins[0])

# 8)

import math
y = ( 1 / (alpha * math.sqrt(2*math.pi)) ) * np.exp( (-1/2)*( (bins[0]-muu)/alpha )**2 )

plt.plot(bins[0],y,'--')
plt.title("Histogramme de la répartition du QI : alpha = 100; muu = 15")
plt.show()

















