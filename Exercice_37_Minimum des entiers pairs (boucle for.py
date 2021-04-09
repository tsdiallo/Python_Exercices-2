L = [int(input("entrer la valeur1\t")), int(input("entrer la valeur2\t")), int(input("entrer la valeur3\t")), int(input("entrer la valeur4\t")), int(input("entrer la valeur5\t"))]


pair=0
n=len(L)
mini=L[0]
for i in range (n):
    if (L[i]%2==0):
        pair=L[i]
        print(pair)
        mini_pair=0
        if (pair< pair+ 1):
                mini_pair=pair  
print (L, "->",mini_pair)
