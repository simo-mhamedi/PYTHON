##created by feecoding

class emploiyer:
    pass
t=list()
n=int(input("Enter Size For Your liste:: Emploeyes:"))
for i in range(n):
    t.append(emploiyer())
    t[i].mat=int(input("Enter Matricule:"))
    t[i].nom=input("Enter  Name:")
    t[i].prenom=input("Enter  Family name:")
    t[i].salair=float(input("Enter  salary:"))
p=0
for i in range(1,n):
    if(t[p].salair<t[p].salair):
        p=i
print(t[p].nom,t[p].prenom)
nom=input("Enter name: ")
prenom=input("Enter  Family name: ")
p1=-1
for i in range(n):
    if(nom==t[i].nom and prenom==t[i].prenom):
        p1=i
if(p1==-1):
    print("Not exes...")
else:
    print(t[p1].mat)
mat=int(input("Enter Matricule:"))
p3=-1
for i in range(n):
    if(t[i].mat==mat):
        p3=i
if(p3==-1):
    print("Not exes...")
else:
    for i in range(p,n-1):
        t[i]=t[i+1]
for i in range(n-1):
    print(t[i].mat)
    print(t[i].nom)
    print(t[i].prenom)
    print(t[i].salair)


