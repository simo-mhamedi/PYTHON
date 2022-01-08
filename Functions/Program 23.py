##created by feecoding

def rechercher(t,d,f,r):
    if(d>f):
        return -1
    m=(d+f)//2
    if(r==t[m]):
        return m
    elif(r>t[m]):
        return rechercher(t,d,m-1,r)
    else:
        return rechercher(t,m+1,f,r)
t=list()
n=int(input("Enter Size For Your Liste:"))
for i in range(n):
    print("Enter item",i+1,":")
    t.append(int(input()))
r=int(input("Enter Your Search...:"))
d=0
f=n-1
print(rechercher(t,d,f,r))
