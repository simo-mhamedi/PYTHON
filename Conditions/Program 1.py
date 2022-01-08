##created by feecoding

n=int(input("enter number of your degree: "))
m=0
for i in range(1,n+1):
    print("enter degree ",i,":")
    notes=float(input())
    m=m+notes
r=m/n
print(r)
print(m)
    
