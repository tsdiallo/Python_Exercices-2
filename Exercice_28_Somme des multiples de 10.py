L = [310, 12, 8100, 90, 31]
s=0
print(L)
for i in (L):
    if(i%10==0):
        s=s+i
print ("la somme s des éléments de L qui sont des multiples de 10 est: \t",s)
print ("tester votre propre liste\t")
L = [int(input("entrer la valeur1\t")), int(input("entrer la valeur2\t")), int(input("entrer la valeur3\t")), int(input("entrer la valeur4\t")), int(input("entrer la valeur5\t"))]

t=0
for i in (L):
    if(i%10==0):
        t=t+i
print ("la somme s des éléments de L qui sont des multiples de 10 est: \t",t)
