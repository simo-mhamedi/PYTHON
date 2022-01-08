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
for i in range(4):
    pg.append(t[i][0])
    pp.append(t[i][0])
    somme.append(t[i][0])
    for j in range(1,5):
        if(pg[i]<t[i][j]):
            pg[i]=t[i][j]
        if(pp[i]>t[i][j]):
            pp[i]=t[i][j]
        somme[i]=somme[i]+t[i][j]
print(pg)
print(pp)
print(somme)
