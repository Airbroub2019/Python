
liste1 = list(range(1,100))

#1)
print("Liste1 = " + str(liste1))

#2)
liste2 = []

for i in range (100,200):
    liste2.append(i)
print("Liste2 = " + str(liste2))
#3)
for i in liste2:
    liste1.append(i)

print("Liste1 après ajout de Liste2 = " + str(liste1))

#4)
liste1.reverse()

print("Liste1 Inverse" + str(liste1))


#5)
liste1.sort()
print("Liste1 trié ordre croissant : " + str(liste1))

#6)
liste3= []
for i in range(1,101):
    if i%2 == 0:
        liste3.append(i)
print("Liste3= " + str(liste3))

#7)
for i in liste3:
    if i%10 == 0:
        liste3.remove(i)
print("Liste3 = " + str(liste3))
#8)
print("Longueur de Liste3 = " + str(len(liste3)))
#9)
print("Multiple de 8 de Liste3 : ")
for i in liste3:
    if i%8 == 0:
        print (i)
#10)
print ("20 premiers elements de Liste3" + str(liste3[0:20]))
#11)
print("20 premiers elements de Liste3" + str(liste3[20:]))
#12)
print("10 derniers elements de Liste3 : " + str(liste3[-10:]))

#13)
liste4 = [x for x in range(1,101) if x%2 != 0]

print ("Liste4=" + str(liste4))
#14)
liste5=[1,1]

[liste5.append(liste5[k-1]+liste5[k-2]) for k in range(2,10)]

print("Liste5= " + str(liste5))

#15)
def mafonctioncallback(callback, liste):
    nouvelle_liste= []
    for element in liste:
        nouvelle_liste.append(callback(element))
    return nouvelle_liste

def carre(x) :
    return x*x
def pariete(x):
    return x%2 == 0
listecarree = mafonctioncallback(carre,liste5)
listepariete = mafonctioncallback(pariete,listecarree)
print("Liste carree : " + str(listecarree))
print("Liste pariete : " + str(listepariete))


def mafonctioncallback2(callback, liste):
    nouvelle_liste= []
    for element in liste:
        if(callback(element)) :
            nouvelle_liste.append(element)
    return nouvelle_liste

listefiltrepair = mafonctioncallback2(pariete,liste5)

print("listefiltrepair= " + str(listefiltrepair))

def mafonctioncallback3(callback, liste):
    nouvelle_liste= []
    sum = liste[0]
    for element in liste[1:]:
           sum = callback(sum,element)
    return sum

def sum(x,y):
    return x+y

def produit(x,y):
    return x*y

sumtotale = mafonctioncallback3(sum,listefiltrepair)
produitotale= mafonctioncallback3(produit,listefiltrepair)
print("Somme Totale : " + str(sumtotale))
print("Produit Totale : " + str(produitotale))

def minMaxMoy(liste):
    min = liste[0]
    max = liste[0]
    sum = 0
    for x in liste:
        if(min>x):
            min = x
        if(max<x):
            max = x
        sum += x

    moyenne = sum/len(liste)
    return min,max,moyenne

listeprincipal = [10,18,14,20,12,16]
minimum,maximum,moyenne=minMaxMoy(listeprincipal)
print("Minimum : " + str(minimum))
print("Maximum : " + str(maximum))
print("Moyenne : " + str(moyenne))

fichier = open("minMaxMoy.txt","w")
fichier.write("minimum = " + str(minimum) + "\nmaximum = " + str(maximum) + "\nmoyenne = " + str(moyenne) )
fichier.close()


#19)

liste6=[1,2,3]

liste6bis = liste6.copy()

liste6bis.append(4)
print("Liste6= " + str(liste6))
print("Liste6Bis= " + str(liste6bis))


