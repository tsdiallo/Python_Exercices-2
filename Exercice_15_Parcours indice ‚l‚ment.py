L = [int(input("entrer la valeur1\t")), int(input("entrer la valeur2\t")), int(input("entrer la valeur3\t")), int(input("entrer la valeur4\t")), int(input("entrer la valeur5\t"))]
longeur=len(L)
#for i in range (longeur):
#    print (i, "->", L[i])

#C'est la meme chose que le "in range in"

for i,j in enumerate(L):
    print(i,"->",j)
