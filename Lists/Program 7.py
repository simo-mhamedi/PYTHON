##created by feecoding

t=list()
for i in range(4):
    t.append(list())
    for j in range(5):
        print("entrer elemnet ",j,":")
        t[i].append(int(input()))
colon=0
lines=0
for i in range(1,4):
    for j in range(1,5):
        if(t[lines][colon]>t[i][j]):
            lines=i
            colon=j
print(lines,colon)
