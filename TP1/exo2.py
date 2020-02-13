#   1)

import numpy as np

#6 de nombre aléatoire
np.random.seed(0)
###


#   2)
arr1 = np.empty(10)
print("Array vide : " + str(arr1))
#   3)
arr2 = np.zeros(10)
print("Array Zeroes : " + str(arr2))
#   4)
arr3 = np.ones(10)
print("Array de Un : " + str(arr3))
#   5)
arr4= np.ones(10)*5
print("Array de Cinq : " + str(arr4))

arr4_bis = np.zeros(10)+5
#   6)
arr5 = np.arange(1,11).astype(str)

print("Array de chaine de caracteres :" + str(arr5))
#   7)
tab1 = np.arange(1,10.5,0.5)
print("Tab1 = " + str(tab1))
#   8)
tab2 = np.linspace(1,10,20)
print("Tab2 = " + str(tab2))
#   9)
tab3 = np.arange(10,30)
print("Tab3 = " + str(tab3))
#   10)
sum = tab3.sum()
print("Somme des entiers de Tab 3 = " + str(sum))
#   11)
sumcumul = tab3.cumsum().sum()
print("Somme cummulés de Tab 3 " + str(sumcumul))
#   12)
moyenne = tab3.mean()
print("Moyenne de Tab3 " + str(moyenne))

#   13)
produitscalaire = np.inner(tab2,tab3)
print("Produit Scalaire entre Tab2 et Tab3 : " + str(produitscalaire))

#   14)

#select1 = np.array(tab3[tab3>20])
select1 = np.extract(tab3>20, tab3)
print("Elements de Tab3 > 20 : " + str(select1))
#   15)
select2 = np.extract((tab3==1) | (tab3==5) | (tab3==10) | (tab3==15),tab3)

print("Elements 1,5,10,15 de Tab3 " + str(select2))

#           LES MATRICES

#   1)
matrixidentity = np.identity(9)
print("Matrice Identité : " + str(matrixidentity))
#   2)
matrixones = np.ones((10,10))

#   3) 4) 5)
print("Taille de la Matrice de 1 : " + str(matrixones.size))
print("Dimension de la Matrice de 1 : " + str(matrixones.ndim))
print("La Matrice de 1 : " + str(matrixones))
#   6)
tmparr = np.arange(9)
matrix = np.reshape(tmparr,(3,3))
print("Matrice 3 x 3 : " + str(matrix))
#   7)
tmpA = np.arange(0.01,1.01,0.01)
A = np.reshape(tmpA,(10,10))
print("A = " + str(A))
#   8)
B = A[6:,0:4]
print("B = " + str(B))
#   9)
matrixonesB = np.ones((B.shape))
print("Matrice de 1 à partir de B : " + str(matrixonesB))
#   10)
C = A[2:4,(0,2,4,6)]
print("C = " + str(C))
#   11)
produitmatriciel = C.dot(B)
print("Produit Matriciel entre B et C = " + str(produitmatriciel))
#   12)
valeurA = A[5,4]
print("Recuperation de la valeur de A : " + str(valeurA))
#  13) 14)
quatriemecolonneA = A[:,3]
print("4eme colonne de A : " + str(quatriemecolonneA))

quatriemeligneA = A[3,:]
print("4eme ligne de A : " + str(quatriemeligneA))
#   15)
newA = A[A[:,3]>0.5]
print("Matrice A dont la 4eme colonne > 0.5 " + str(newA))

#   16)
moyennematrix = newA.mean()
print("Moyenne globale de la nouvelle matrice A : " + str(moyennematrix))
#   17) 18)
moyenneeachrow = np.mean(A,axis=1)
print("Moyenne de chaque ligne de la matrice A : " + str(moyenneeachrow))
#   19)
produitscalaireA = np.inner((A[0,:]),(A[:,0]).reshape((A[0,:]).size))
print("Produit Scalaire 1ere colonne A x 1eme ligne A : " + str(produitscalaireA))
#   20)
A[3:7,3:7] = 0

print("A avec des valeurs 0 au millieu : " + str(A))
#   21)
indexing = np.where(A==0)
print("Recuperation des indexe de la valeurs 0 dans A : " + str(indexing))

#           NOMBRE ALEATOIRES

#   1)
randarr = np.random.rand(10)
print("Numpy Array de 10 valeurs aléatoires : " + str(randarr))
#   2)
randarr2 = (np.random.rand(100)*100).astype(int)
print("Numpy Array de 100 valeurs entre 0 et 100 : " + str(randarr2))
#   3)
randarr3 =  np.random.normal(0, 0.1, 25)
print("Distribution normale centrée réduite : " + str(randarr3))


#   4)
randarr4 = np.random.uniform(-1,0,25)
print("Uniforme : " + str(randarr4))


#  LES ENTREES/SORTIES 1) 2)
randmatrix = np.random.rand(10,10)
print("Matrice random 10 x 10 " + str(randmatrix))

np.savetxt("matrice1.csv",randmatrix, delimiter=";")

Text = np.genfromtxt("matrice1.csv")
