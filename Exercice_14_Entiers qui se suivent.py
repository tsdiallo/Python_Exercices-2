x = int(input("entrer la valeur de x \n"))
y = int(input("entrer la valeur de y \n"))
ok = (((x == 1 and y == 4) or (x == 4 and y == 1)) or (x == y + 1 or y == x+ 1) and (x >= 1 and x <=4)and(y >= 1 and y <=4))
print("x = ",x,", y =",y, "->", " ok = ", ok)
