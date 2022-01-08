##created by feecoding

t=list()
n=int(input("Enter Size For Your Liste:"))
for i in range(n):
    print("Enter item",i+1,":")
    t.append(int(input()))
for i in range(n):
    carre=t[i]**2
    for j in range(n):
        if(carre==t[j]):
            print(t[j])

    
        
