a=int(input("entrer la valeur de a: "))
b=int(input("entrer la valeur de b: "))
while a<b:
    a=int(input("entrer une valeur de a supérieure à celle b: "))
    b=int(input("entrer la valeur de b inférieure à celle de a: "))
for i in range (a,b-1,-1):
    print (i)
