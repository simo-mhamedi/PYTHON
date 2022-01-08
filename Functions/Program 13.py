##created by feecoding

def rec(t,r,d,f):
    if(d>f):
        return -1
    v=(d+f)//2
    if(t[v]==r):
        return v
    elif(r<t[v]):
        return rec(t,r,v+1,f)
    return rec(t,r,d,v-1)
t=list()
n=int(input("Enter the size: "))
for i in range(n):
    print("Enter the elements of the list: ")
    t.append(int(input()))
r=int(input("Enter the value your looking for: "))
d=int(input('entrer:'))
f=len(t)
print(rec(t,r,d,f))
