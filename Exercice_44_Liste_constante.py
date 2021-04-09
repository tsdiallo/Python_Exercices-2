L = [42, 42, 42]
L = [42, 421, 42, 42]

tousEgaux=True
i=0
while i+1 in range(len(L)):
    if L[i+1] != L[i]:
        tousEgaux=False
    i+=1
print(tousEgaux)
