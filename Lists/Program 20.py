##created by feecoding

t=list()
n=int(input("Enter Size For Your liste:")
for i in range(n):
    print("Enter item",i+1,":")
    t.append(int(input()))
p=int(input("Enter position For Delet.. it :"))
for i in range(p,n-1):
    t[i]=t[i+1]
for i in range(n-1):
    print(t[i])
