a = int(input("Entrer la valeur de a \n"))
b = int(input("Entrer la valeur de b \n"))
m = int(input("Entrer la valeur de m \n"))
resultat=(m % a)%b==0
if resultat == True :
    print("on peut régler m = ", m, " puisque",128, " = ",((m % a) // b), "*", b, "+",(m//a),"*",a)
else: print("on ne peut pas régler m =",m,"unités")
