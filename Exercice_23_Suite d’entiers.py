n=int(input("entrer une valeur n"))
d=10
if (n==1):
    print (n, "->", d)
else:
    for i in range (2,n+1):
        d=(d*2)+1
    print (n, "->", d)
    
