L = [int(input("entrer la valeur1\t")), int(input("entrer la valeur2\t")), int(input("entrer la valeur3\t")), int(input("entrer la valeur4\t")), int(input("entrer la valeur5\t"))]
n=len(L)
n_pair=0
n_impair=0
for i in range (n):
    if(L[i]%2==0):
        n_pair=n_pair+1
    elif(L[i]%2!=0):
        n_impair=n_impair+1
print ("le nombre n_pair d’indices i tel que l’élément L[i] est pair:\t", n_pair)
print ("— le nombre n_impair d’indices i tel que l’élément L[i] est impair:\t", n_impair)
