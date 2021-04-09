def suiteV(U):
    V=""
    for i in U:
        val=int(i)^1
        V+=str(val)
    return V
U="0"
for j in range(1,4):
    U=str(U)+str(suiteV(U))
print (U)
