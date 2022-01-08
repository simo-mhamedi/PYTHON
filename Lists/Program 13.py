##created by feecoding

t=list()
n=int(input('Input:'))
for i in range(n):
    print("Input :")
    t.append(int(input()))
for i in range(n-1):
    p=i
    for j in range(i+1,n):
        if(t[p]>t[j]):
            p=j
    if(p!=i):
        r=t[p]
        t[p]=t[i]
        t[i]=r
print(t)
