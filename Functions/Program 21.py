##created by feecoding

def parfait(n):
    d=0
    for i in range(1,n//2+1):
        if(n%i==0):
            d=d+i
    return d
n=int(input("Entrer  Number:"))
for i in range(1,n):
    d=parfait(i)
    if(d==i):
        print(i)
