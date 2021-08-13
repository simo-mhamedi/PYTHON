n=int(input("entrer nomber de votre notes:"))
m=0
for i in range(1,n+1):
    print("entrer la note",i,":")
    notes=float(input())
    m=m+notes
r=m/n
print(r)
print(m)
    
