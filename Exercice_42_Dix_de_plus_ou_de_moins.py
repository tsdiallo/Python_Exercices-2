l = [42, 32, 22, 32, 42, 52, 72]
ok=True
i=0
while i+1 in range(len(l)):
    if l[i+1] not in (l[i]+10, l[i]-10):
        ok=False

    i+=1
    
print(ok)
