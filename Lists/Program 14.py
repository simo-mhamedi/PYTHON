##created by feecoding

t=list()
n=int(input("Enter Size For Your Liste:"))
for i in range(n):
    print("Enter item",i+1,":")
    t.append(int(input()))
for i in range(n//2):
    rv=t[i]
    t[i]=t[n-1-i]
    t[n-1-i]=rv
print(t)
