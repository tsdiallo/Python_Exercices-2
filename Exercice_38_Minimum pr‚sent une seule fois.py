L = [int(input("entrer la valeur1\t")), int(input("entrer la valeur2\t")), int(input("entrer la valeur3\t")), int(input("entrer la valeur4\t")), int(input("entrer la valeur5\t"))]
mini=L[0]
n=len(L)
a=0
for i in range(n):
    if (L[i]< mini):
        mini=L[i]
print ("mini=\t",mini)
for i in range (n):
        if (mini==L[i]):
                a+=1
        
if (a==1):
        miniUnique= True
        print ("et mini apparaît une seule fois dans la liste:\t",miniUnique)
else:
        miniUnique= False
        print ("et mini apparaît une seule fois dans la liste:\t",miniUnique)
    
