##created by feecoding

t=list()
for i in range(20):
    print("Type element ",i+1,":")
    t.append(int(input()))
ma=t[0]
for i in range(1,20):
    if(ma<t[i]):
        ma=t[i]
print(ma)
