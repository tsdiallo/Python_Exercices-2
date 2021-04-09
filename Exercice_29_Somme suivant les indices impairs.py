L=[31, 12, 81, 9, 31]
s=0
print(L)
n=len(L)
for i in range (n):
    if (i%2!=0):
        s=s+L[i]
print ("la somme s des éléments de L dont l’indice est impair est: \t",s)

print ("tester votre propre liste\t")
L = [int(input("entrer la valeur1\t")), int(input("entrer la valeur2\t")), int(input("entrer la valeur3\t")), int(input("entrer la valeur4\t")), int(input("entrer la valeur5\t"))]
t=0
n=len(L)
for i in range (n):
    if (i%2!=0):
        t=t+L[i]
print ("la somme s des éléments de L dont l’indice est impair est: \t",t)

