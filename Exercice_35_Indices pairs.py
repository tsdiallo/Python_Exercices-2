L = [int(input("entrer la valeur1\t")), int(input("entrer la valeur2\t")), int(input("entrer la valeur3\t")), int(input("entrer la valeur4\t")), int(input("entrer la valeur5\t"))]
n=len(L)
IP=[]
II=[]
for i in range (n):
    if(i%2==0):
        IP.append(L[i])
    else:
        II.append(L[i])
print ("la liste IP des éléments de L d’indices pairs\t",IP)        
print ("la liste II des éléments de L d’indices impairs\t",II)
