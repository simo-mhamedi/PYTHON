##created by feecoding

def plus(t,n):
    p=t[0]
    for i in range(1,n):
        if(p<t[i]):
            p=t[i]
    return p
n=int(input("type the size of your list: "))
t=list()
for i in range(n):
    print("input :")
    t.append(int(input()))
print(plus(t,n))
