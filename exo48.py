#partie 1
c="ababa"

def nombre_occ_a(c):
    cpt=0
    for i in c:
        if i=="a":
            cpt+=1
    return cpt
print(nombre_occ_a("ababa"))

#partie 2

cpt1=0
cpt2=0
for i in c:
    if i=="a":
        cpt1+=1
    else:
        cpt2+=1
if cpt1>cpt2:
    print("a")
else:
    print("b")
