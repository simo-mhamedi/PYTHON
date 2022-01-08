##created by feecoding

class telefone:
    pass
def lire_contacte():
    c=telefone()
    c.name=input("Enter  Name:")
    c.prenom=input("Enter  Family name:")
    c.nemero=int(input("Enter  Family Serie Number:"))
    return c
def afficher(r):
    print(r.name)
    print(r.prenom)
    print(r.nemero)
def ajouter(t,n,u):
    t.append(u)
    return t
def rechercher(t,n,nom,prenom):
    p=-1
    for i in range(n):
        if(t[i].name==nom and t[i].prenom==prenom):
            p=i
            i=n
    return p
def delet(t,n,s):
    for i in range(s,n-1):
        t[i]=t[i+1]
    return t
t=list()
n=0
while True:
    print("1 : FOR ADD contact:")
    print("2 : FOR DELETE  contact:")
    print("3 : FOR SEARCH  contact:")
    print("4 : FOR SHOW ALL contacts:")
    print("5 : FOR LEAVE programme:")
    c=int(input())
    if(c==1):
        g=lire_contacte()
        t=ajouter(t,n,g)
        n=n+1
    elif(c==2):
        ns=input("Enter  Name For Delet...:")
        ps=input("Enter  Family Name For Delet...:")
        q=rechercher(t,n,ns,ps)
        if(q==-1):
            print("Not exes...")
        else:
            t=delet(t,n,q)
            n=n-1
    elif(c==3):
        nr=input("Enter  Name For Search...:")
        pr=input("Enter  Family Name For Search...:")
        f=rechercher(t,n,nr,pr)
        if(f==-1):
            print("Not exes...")
        else:
            print(t[f].nemero)
    elif(c==4):
        for i in range(n):
            print(afficher(t[i]))
    else:
        print("Done")
        break
