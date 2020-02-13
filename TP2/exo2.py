import matplotlib.pyplot as plt
import numpy as np
# 1)
x=np.array([1,4,8,9])
y=np.array([12,25,34,78])

plt.scatter(x,y)
plt.title("Nuage de points")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 2)
x=np.random.rand(1000)
y=np.random.rand(1000)
plt.scatter(x,y)
plt.title("Nuage de points aléatoire 1000 valeurs")
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# 3)
x=np.array([1,4,8,9])
y=np.array([12,25,34,78])
plt.plot(x,y,"g")
plt.title("Courbe")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 4)

x=np.random.randn(100)
y=np.random.randn(100)
plt.plot(x,y,"g")
plt.title("Courbe aléatoire")
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# 5) 6) 7) 8) 9) 10)
x=np.linspace(0,2,100)

plt.plot(x,x,"b", label="x linéaire")
plt.plot(x,x**2,"orange", label="x carré")
plt.plot(x,x**3,"g", label="x cubique")
plt.title("Comparaison des fonctions linéaire, quadratique et cubique")
plt.xlabel('abscisse')
plt.ylabel('ordonnée')
plt.legend()
plt.show()

# 9) 10)
x=np.linspace(0,2,100)
fig, axes = plt.subplots(nrows=1,ncols=3,figsize=(12,6))
axes[0].plot(x,x,"b", label="x linéaire")
axes[0].set_title("courbe linéaire")
axes[1].plot(x,x**2,"orange", label="x carré")
axes[1].set_title("courbe carré")
axes[2].plot(x,x**3,"g", label="x cubique")
axes[2].set_title("courbe cubique")

plt.show()

# 11)

x=np.random.uniform(0,10,100)

plt.hist(x)

plt.show()









