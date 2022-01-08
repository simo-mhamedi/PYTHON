##created by feecoding

ch=list()
n=int(input("Enter Size For Your liste:"))
for i in range(n):
    print("Enter String",i+1,":")
    ch.append(input())
b=True
for i in range(n-1):
    if(ch[i]>ch[i+1]):
        b=False
if(b==True):
    print("alphabetical")
else:
    print("Not alphabetical")
