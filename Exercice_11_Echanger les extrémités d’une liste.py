print("avant permutation")
L = [int(input("entrer la valeur1\t")), int(input("entrer la valeur2\t")), int(input("entrer la valeur3\t")), int(input("entrer la valeur4\t")), int(input("entrer la valeur5\t"))]
print (L)
x=L[0]
L[0]=L[4]
L[4]=x
print("apres permutation")
print (L)
