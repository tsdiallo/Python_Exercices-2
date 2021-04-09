n=int(input("entrer la valeur n\t"))
s=0
for i in range (n,0,-1):
    if (i%2!=0):
        s=s-i
    else:
        s=s+i
print (s)
