l = [10, 20, 40, 80]
l = [10, 40, 80]
ok=True
i=0
while i+1 in range(len(l)):
    if l[i+1] != l[i]*2:
        ok=False
    i+=1
    
print(ok)
