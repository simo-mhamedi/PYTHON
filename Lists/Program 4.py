##created by feecoding

t=list()
s=0
for i in range(20):
    print("Type element ",i+1,":")
    t.append(int(input()))
    s=s+t[i]
m=s//20
compt=0
for i in range(20):
    if(t[i]>m):
        compt=compt+1
print(m)
print(compt)
