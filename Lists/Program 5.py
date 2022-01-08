##created by feecoding

t=list()
for i in range(5):
    t.append(list())
    for j in range(4):
        print("Type element ",j+1,":")
        t[i].append(int(input()))
s=0
for i in range(5):
    for j in range(4):
        s=s+t[i][j]
print(s)
