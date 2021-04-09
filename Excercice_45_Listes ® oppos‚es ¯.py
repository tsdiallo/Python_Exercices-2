l = [81, -12]
m = [-81, -12]

sontOpposees = True

if len(l)==len(m):
    for i in range(len(l)):
        if m[i]!=-l[i]:
            sontOpposees = False
print(sontOpposees)
