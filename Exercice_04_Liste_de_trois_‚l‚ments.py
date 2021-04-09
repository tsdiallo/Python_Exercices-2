entierx=int(input("Entrer le chiffre à trois elements \t"))
Liste=[]
Liste.append(entierx)
for i in range (1,3):
    entierx+=10
    Liste.append(entierx)
print ("De 10 en 10 jusqu'au troisième élément on a: ",Liste)
