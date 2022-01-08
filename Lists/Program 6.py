##created by feecoding

t=list()
for i in range(4):
    t.append(list())
    for j in range(5):
        print("Type element",j+1,':')
        t[i].append(int(input()))
pg=t[0][0]
for i in range(4):
    for j in range(1,5):
        if(pg<t[i][j]):
            pg=t[i][j]
print(pg)
