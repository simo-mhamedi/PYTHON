##created by feecoding

t=list()
t2=list()
s=list()
for i in range(5):
    print("Enter item",i+1,":")
    t.append(int(input()))
print("--------Second list------------")
for j in range(5):
    print("Enter item",j+1,":")
    t2.append(int(input()))
for i in range(5):
    s.append(t[i]+t2[i])
print(s)
