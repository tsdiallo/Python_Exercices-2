L = [int(input("entrer la valeur1\t")), int(input("entrer la valeur2\t")), int(input("entrer la valeur3\t")), int(input("entrer la valeur4\t")), int(input("entrer la valeur5\t"))]
mini=L[0]
n=len(L)
for i in range(n):
    if (L[i]< mini):
        mini=L[i]
print ("Le plus petit element de la liste est:\t",mini)
