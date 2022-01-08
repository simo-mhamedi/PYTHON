class salarier:
    pass
def sisir(t,n):
    for i in range(n):
       t.append(salarier())
       t[i].nom=input("Enter  Name:")
       t[i].prenom=input("Enter  Family name:")
       t[i].salair=float(input("Enter  Salair:"))
    return t
def trier(t,n):
    c=salarier()
    for i in range(n-1):
        p=i
        for j in range(i+1,n):
           if(t[p].nom>t[j].nom):
               p=j
        if(p!=i):
            c=t[p]
            t[p]=t[i]
            t[i]=c
    return t
def afficher(c):
    print(c.nom)
    print(c.prenom)
    print(c.salair)
t=list()
while True:
    print("FOR ENTER 1:")
    print("FOR TO SOURT 2:")
    print("FOR SHOW 3:")
    print("FOR LEAVE 4:")
    c=int(input())
    if(c==1):
        n=int(input("Enter Size For Your liste:"))
        t=sisir(t,n)
    elif(c==2):
        t=trier(t,n)
    elif(c==3):
        for i in range(n):
            print(afficher(t[i]))
    else:
        print("Done")
        break
