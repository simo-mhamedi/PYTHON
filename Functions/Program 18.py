##created by feecoding

def pussance(n,p):
    if(p==0):
        return 1
    else:
        return n*pussance(n,p-1)
n=int(input("Enter n:"))
p=int(input("Enter p:"))
print(pussance(n,p))
