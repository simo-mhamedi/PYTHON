##created by feecoding

def some(t,n):
    s=0
    for i in range(n):
        s=s+t[i]
    return s
t=list()
n=int(input('Type the size of your list: '))
for i in range(n):
    print("input:")
    t.append(int(input()))
print(some(t,n))
