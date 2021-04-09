l = ["boire", "chanter", "fuir", "voir", "avancer", "lire"]
for i in l:
    if i[len(i):len(i)-3:-1] =="re":
        print(i)
