a = int(input("valeur a de l'equation\t"))
b = int(input("valeur b de l'eqation\t"))
c = int(input("valeur 1 de l'equation\t"))
delta = b*b -4*a*c
if delta >0:
    print("2 solutions distinctes :")
    x1=(-b - delta**0.5)/(2.*a)
    x2=(-b + delta**0.5)/(2.*a)
    S=[x1,x2]
    print ("S =\t",S)
elif delta == 0:
    print("une seule solution")
    x=(-b)/(2.*a)
    S=[x]
    print("S =\t",S)
else:
    print("Aucune solution")
    S=[]
    print (S)
