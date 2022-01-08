##created by feecoding

def imapair(t,n):
    d=0
    for i in range(n):
        if(t[i]%2!=0):
            d=d+1
    return d
t=list()
n=int(input("Enter Size For Your liste:"))
for i in range(n):
    print("Enter item",i+1,":")
    t.append(int(input()))
print(imapair(t,n))
