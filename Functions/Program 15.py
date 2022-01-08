##created by feecoding

def div(n):
    lis=list()
    for i in range(1,n+1//2):
        if(n%i==0):
            lis.append(i)
    print(lis)
n=int(input("Enter Number:"))
print(div(n))
