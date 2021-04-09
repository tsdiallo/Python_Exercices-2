print("avant permutation")
L = [int(input("entrer la valeur1\t")), int(input("entrer la valeur2\t")), int(input("entrer la valeur3\t")), int(input("entrer la valeur4\t")), int(input("entrer la valeur5\t"))]
x= len(L)-1  
position=0
print (L)
while(position<x):
    L[position],L[position+1]=L[position+1],L[position]
    position+=2

print("apres permutation")
print (L)
