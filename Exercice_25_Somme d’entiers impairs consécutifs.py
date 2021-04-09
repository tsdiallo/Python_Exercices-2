N=int(input("enter un entier positif \t"))
s=0
for i in range(2*N):
    if(i%2!=0):
        s=s+i
print ("La somme des N premiers entiers impairs est:\t",s)
