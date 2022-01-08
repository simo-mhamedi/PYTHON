##created by feecoding

def premier(a):
    b=True
    for i in range(2,a+1//2):
        if(a%i==0):
            b=False
    return b
n=int(input("Type the number: "))
d=premier(n)
if(d==True):
    print("premium")
else:
    print("not premium")
    
