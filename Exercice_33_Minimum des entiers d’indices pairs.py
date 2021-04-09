L = [int(input("entrer la valeur1\t")), int(input("entrer la valeur2\t")), int(input("entrer la valeur3\t")), int(input("entrer la valeur4\t")), int(input("entrer la valeur5\t"))]
mini_pairs=L[0]
n=len(L)
for i in range(n):
    if (L[i]< mini_pairs and i%2==0):
        mini_pairs=L[i]
print(" mini_pairs=",mini_pairs)
