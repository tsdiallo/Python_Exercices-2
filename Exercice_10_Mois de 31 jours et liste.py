m=int(input("entrer un numéro d'un mois \t"))
est_mois_31=[1,3,5,7,8,10,12]
while (m<=0 and m>12):
    print("Le nombre de mois est compris entre 1 et 12")
    m=int(input("entrer un numéro d'un mois \t"))

if (m not in est_mois_31):
    print("\t le mois saisi n'est pas a 31 jours")
else:
    print("\t le mois saisi est a 31 jours")
