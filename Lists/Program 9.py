##created by feecoding

t=list()
for i in range(4):
    t.append(list())
    for j in range(5):
        print("enter element:")
        t[i].append(int(input()))
pg=list()
pp=list()
somme=list()
for j in range(5):
    pg.append(t[0][j])
    pp.append(t[0][j])
    somme.append(t[0][j])
    for i in range(1,4):
        if(pg[j]<t[i][j]):
            pg[j]=t[i][j]
        if(pp>t[i][j]):
            pp=t[i][j]
        somme[j]=somme[j]+t[i][j]
print(pg)
print(pp)
print(somme)
