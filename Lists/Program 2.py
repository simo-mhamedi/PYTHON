##created by feecoding

t1=list()
t2=list()
t3=list()
for i in range(4):
    print("Type element ",i,":")
    t1.append(int(input()))
for j in range(4):
    print("Type an other element ",j,":")
    t2.append(int(input()))
for i in range(4):
    if(t1[i]%t2[i]==0):
        t3.append(0)
    else:
        t3.append(1)
print(t1)
print(t2)
print(t3)
