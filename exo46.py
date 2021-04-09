L = [82, 81, 83]

consecutifs=True
i=0
while i+1 in range(len(L)):
    if L[i+1] != L[i]+1:
        consecutifs=False
    i+=1
print(consecutifs)
