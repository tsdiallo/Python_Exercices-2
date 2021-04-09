L=[int(input("entrer la valeur1\t")), int(input("entrer la valeur2\t")), int(input("entrer la valeur3\t")), int(input("entrer la valeur4\t")), int(input("entrer la valeur5\t")), int(input("entrer la valeur6\t")), int(input("entrer la valeur7\t")), int(input("entrer la valeur8\t")), int(input("entrer la valeur9\t")), int(input("entrer la valeur10\t"))]
n=len(L)
for i in range (n-1):
    if(L[i+1] > L[i]):
        v="augmente"
        print (v)
    else:
        v="diminue"
        print (v)
    
