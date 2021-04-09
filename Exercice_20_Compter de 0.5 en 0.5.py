a=int(input("entrer la valeur de a \t"))
b=int(input("entrer la valeur de b \t"))
def frange(debut, fin, pas):
    i = debut
    while i <= fin:
        yield i
        i += pas

for i in frange(a, (b), 0.5):
    print(i,end=" ")
