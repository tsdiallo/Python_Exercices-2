x=int(input("Entrer une valeur pour un test a l'unité près:\t"))
L =[31,76,12,73,42,83,9,91,65,45,54,13,58,43,21,97]
ok=(x in L or x-1 in L or x+1 in L)
print(ok)
