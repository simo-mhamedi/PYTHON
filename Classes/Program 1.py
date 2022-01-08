##created by feecoding

class enployer:
    pass
t=list()
for i in range(5):
    t.append(enployer())
    print("Enter the name: ")
    t[i].nom=(input())
    t[i].prenom=(input())
    t[i].salair=(int(input()))
p=0
for i in range(1,5):
    if(t[p].salair<t[i].salair):
        p=i
print(t[p].nom,t[p].prenom)
