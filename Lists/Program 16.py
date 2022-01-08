##created by feecoding

t=list()
t2=list()
for i in range(4):
    print("Enter item",i+1,":")
    t.append(int(input()))
print("--------Second list------------")
for j in range(4):
    print("Enter item",j+1,":")
    t2.append(int(input()))
s=0
for i in range(4):
    for j in range(4):
        s=s+t[i]*t2[j]
print(s)
