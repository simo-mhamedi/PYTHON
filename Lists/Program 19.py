##created by feecoding

t=list()
n=int(input("Enter Size For Your liste:"))
for i in range(n):
    print("Enter item",i+1,":")
    t.append(int(input()))
p=int(input("Enter position:"))
t.append(0)
for i in range(n,p,-1):
    t[i]=t[i-1]
x=int(input("Enter item For Modif... it into list"))
t[p]=x
print(t)
