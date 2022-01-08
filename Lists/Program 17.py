##created by feecoding

t=list()
n=int(input("Enter Size For Your liste:"))
for i in range(n):
    print("Enter item",i+1,":")
    t.append(int(input()))
x=int(input("Enter item For Modif... it into list"))
t.append(0)
t[n]=x
print(t)
