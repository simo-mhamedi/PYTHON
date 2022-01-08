##created by feecoding

def somme(t,n):
    if(n==0):
        return 0
    else:
        return t[n-1]+somme(t,n-1)
t=list()
n=int(input("Enter Size For Your liste:"))
for i in range(n):
    print("Enter item",i+1,":")
    t.append(int(input()))
print(somme(t,n))
