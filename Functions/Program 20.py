##created by feecoding

def parfait(n):
    d=0
    for i in range(1,n//2+1):
        if(n%i==0):
            d=d+i
    return d
n=int(input("Enter  Number:"))
d=parfait(n)
if(d==n):
    print("True")
else:
    print("False")
