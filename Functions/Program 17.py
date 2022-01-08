##created by feecoding

def indice(t,n,x):
    p=0
    for i in range(n):
        if(t[i]==x):
            p=i
            i=n
    return p 
t=list()
n=int(input("Enter Size For Your liste:"))
for i in range(n):
    print("Enter item",i+1,":")
    t.append(int(input()))
x=int(input("Enter:"))
print(indice(t,n,x))
