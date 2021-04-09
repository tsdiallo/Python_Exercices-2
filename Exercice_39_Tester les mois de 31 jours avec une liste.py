x=int(input("Entrer un chiffre\n"))
jours=[1,3,5,7,9,11]
n=len(jours)
for i in range(n-1):
    mois31=(x in jours )
print("le mois",i,"possede 31 jours",mois31)
