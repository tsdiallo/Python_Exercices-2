L = [int(input("entrer la valeur1\t")), int(input("entrer la valeur2\t")), int(input("entrer la valeur3\t")), int(input("entrer la valeur4\t")), int(input("entrer la valeur5\t"))]
x=0
n=len(L)
print("Avant permutation")
print (L)
while(x<=(n//2)):
    L[x],L[-1-x]=L[-1-x],L[x]
    x+=1
print("Apres permutation")
print (L)
