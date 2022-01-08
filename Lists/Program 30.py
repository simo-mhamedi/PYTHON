##created by feecoding

t=list()
n=int(input("Enter Size For Your Liste:"))
for i in range(n):
    print("Enter item",i+1,":")
    t.append(int(input()))
for i in range(n):
    tripal=t[i]*3
    for j in range(n):
        if(tripal==t[j]):
            print(t[i])
            
            
            
