# 1)
import numpy as np

redwine=np.genfromtxt('redwine.csv',delimiter=';')

whitewine=np.genfromtxt('whitewine.csv',delimiter=';')




# 2-3
import matplotlib.pyplot as plt

x=redwine[:,11]
y=redwine[:,10]

plt.scatter(x,y)

plt.title("[redwine] Courbe du degré d'alcool en fonction de sa qualité")
plt.xlabel("Qualité d'lacool")
plt.ylabel("Degré d'alcool")

# 4
#plt.boxplot(,showmeans=True)
#plt.show()

Listex= [3,4,5,6,7,8]
Listey = []
for i in Listex:
    Listey.append(y[x==i].mean())

plt.plot(Listex, Listey, "red")

plt.show()



#5)
x=whitewine[:,11]
y=whitewine[:,10]

plt.scatter(x,y)
plt.title("[whitewine]Courbe du degré d'alcool en fonction de sa qualité")
plt.xlabel("Qualité d'lacool")
plt.ylabel("Degré d'alcool")



Listex2= [3,4,5,6,7,8,9]
Listey2 = []
for i in Listex2:
    Listey2.append(y[x==i].mean())

plt.plot(Listex2, Listey2, "g")

plt.show()

#6)

plt.plot(Listex, Listey, "red")

plt.plot(Listex2, Listey2, "g")
plt.title("Comparaison moyenne ")
plt.xlabel("Qualité d'lacool")
plt.ylabel("Moyenne")
plt.show()


# 7)

x=redwine[:,11]
y=whitewine[:,11]
Lista = [x,y]
plt.boxplot(Lista)
plt.show()









