class date:
    pass
class liver:
    pass
t=list()
for i in range(5):
    t.append(liver())
    t[i].titre=input("Enter the title: ")
    t[i].auteur=input("Enter the author: ")
    t.append(date())
    t[i].jour=int(input("Day: "))
    t[i].mois=int(input("Month: "))
    t[i].anne=int(input("Year: "))
p=0
for i in range(1,5):
    if(t[p].anne>t[i].anne):
        p=i
    elif(t[p].anne==t[i].anne and t[p].mois>t[i].mois):
        p=i
    elif(t[p].anne==t[i].anne and t[p].mois==t[i].mois and t[p].jour>t[i].jour):
        p=i
print(t[p].titre)



