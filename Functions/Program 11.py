##created by feecoding

def lookup(t,n,r):
    p=-1
    for i in range(n):
        if(r==t[i]):
            p=i
    return p
t=list()
n=int(input("Enter the size of your list: "))
for i in range(n):
    print("Enter the elements of your list: ")
    t.append(int(input()))
r=int(input('Enter the value your looking for: '))
f=lookup(t,n,r)
if(f==-1):
    print("Error")
else:
    print(t[f])
