##created by feecoding

class salarier:
    pass
def sisie():
    c=salarier()
    c.matricule=int(input("Enter  matricule:"))
    c.nom=input("Enter  Name:")
    c.prenom=input("Enter  Family name:")
    c.salair=float(input("Enter  Salair:"))
    return c
def affecher(t,n):
    for i in range(n):
        print(t[i].matricule)
        print(t[i].nom)
        print(t[i].prenom)
        print(t[i].salair)
def tirer(t,n):
    r=salarier()
    for i in range(n-1):
        p=i
        for j in range(i+1,n):
            if(t[p].nom>t[j].nom):
                p=j
        if(p!=i):
            r=t[p]
            t[p]=t[i]
            t[i]=r
    return t
t=list()
n=0
while True:
    print("1 : FOR ADD Salarié:")
    print("2 : FOR  Trier  salariés With ordre alphabétique:")
    print("3 : FOR SHOW ALL Salariés:")
    print("4 : FOR LEAVE programme:")
    c=int(input())
    if(c==1):
        t.append(salarier())
        g=sisie()
        t[n]=g
        n=n+1
    elif(c==2):
        t=tirer(t,n)
    elif(c==3):
        affecher(t,n)   
    else:
        print("Done")
        break
