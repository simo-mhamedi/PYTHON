##created by feecoding

def lookup(t,n,r):
    debut=0
    final=n
    m=(debut+final)//2
    while(debut<=final):
        if(r==t[m]):
            return m
        elif(r>t[m]):
            debut=m+1
        else:
            final=m-1
        m=(debut+final)//2
    return -1
t=list()
n=int(input("Enter the size of your list: "))
for i in range(n):
    print("Enter the elements of your list")
    t.append(int(input()))
r=int(input('Enter the value your looking for: '))
f=lookup(t,n,r)
if(f==-1):
    print("Error")
else:
    print(t[f])
        
