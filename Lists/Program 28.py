##created by feecoding

t=list()
for i in range(4):
    t.append(list())
    for j in range(4):
        print("Enter string",i+1,':'")
        t[i].append(int(input()))
b=True
for i in range(1,4):
    for j in range(i-1):
        if(t[i][j]!=0):
            b=False
if(b==True):
    print("Superior")
else:
    print("Inferior")
