##created by feecoding

def rechercher(t,n,r):
    d=0
    f=n-1
    m=(d+f)//2
    while (d<=f):
        if(r==t[m]):
            return m
        elif(r<t[m]):
            d=m+1
        else:
            f=m-1
        m=(d+f)//2
t=list()
n=int(input("Enter Size For Your Liste:"))
for i in range(n):
    print("Enter item",i+1,":")
    t.append(int(input()))
r=int(input("Enter Your Search...:"))
print(rechercher(t,n,r))

            
