#   1)

import numpy as np

#6 de nombre aléatoire
np.random.seed(0)
###

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

#   5)

randmatrix = np.random.rand(10,10)
print("Matrice random 10 x 10 " + str(randmatrix))

#  LES ENTREES/SORTIES 1) 2)


np.savetxt("matrice1.csv",randmatrix, delimiter=";")

Text = np.genfromtxt("matrice1.csv")
