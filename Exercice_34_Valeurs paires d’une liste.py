L = [int(input("entrer la valeur1\t")), int(input("entrer la valeur2\t")), int(input("entrer la valeur3\t")), int(input("entrer la valeur4\t")), int(input("entrer la valeur5\t"))]
n=len(L)
P=[]
I=[]
for i in range (n):
    if(L[i]%2==0):
        P.append(L[i])
    else:
        I.append(L[i])
print ("la liste P des entiers pairs\t",P)        
print ("la liste I des entiers impairs\t",I)
