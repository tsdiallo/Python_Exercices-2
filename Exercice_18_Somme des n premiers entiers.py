n=int(input("entrer un nombre entier positif \t"))
s=0
for i in range (1,n+1):
    s=s+i
print ("1+2+...+n =\t",s)
if (s==(n*(n+1))/2):
    s=True
    print("Le resultat obtenu est egale a (n*(n+1))/2")
    print (s)
else:
    s=False
    print("Le resultat obtenu est different de (n*(n+1))/2")
    print (s)
