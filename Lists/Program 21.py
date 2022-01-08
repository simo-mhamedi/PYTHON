##created by feecoding

t=list()
for i in range(4):
    t.append(list())
    for j in range(4):
        print("Enter item :")
        t[i].append(int(input()))
s=0
for i in range(4):
    s=s+t[i][i]
print(s)
