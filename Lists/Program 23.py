##created by feecoding

t=list()
for i in range(5):
    t.append(list())
    for j in range(5):
        print("Enter item :")
        t[i].append(int(input()))
b=True
for i in range(1,5):
    for j in range(i-1):
        if(t[i][j]!=0):
            b=False
if(b==True):
    print("superieur")
else:
    print("inferierr")

