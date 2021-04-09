from math import pow    
n=int(input("entrer un nombre entier positif \t"))
s=0
for i in range (1,n+1):
    s+=10**(i-1)
print ("1 + 10 + ... + 10n-1 =\t",s)
if (s==((10**n)-1)/9):
    s=True
    print("Le resultat obtenu est egale a (n*(n+1))/2")
    print (s)
else:
    s=False
    print("Le resultat obtenu est different de (n*(n+1))/2")
    print (s)
