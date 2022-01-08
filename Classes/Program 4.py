##created by feecoding

class stagair:
    pass
t=list()
n=0
while True:
    print("1:ADD a trainner")
    print("2:Edit a trainner")
    print("3:DELETE a trainner")
    print("4:List")
    print("5:Quit")
    c=int(input())
    if(c==1):
        t.append(stagair())
        n=n+1
        t[n-1].nom=input("Enter first name: ")
        t[n-1].prenom=input("Enter  Family name: ")
        t[n-1].note1=int(input("Enter note 1: "))
        t[n-1].note2=int(input("Enter note 2: "))
        t[n-1].note3=int(input("Enter note 3: "))
    elif(c==2):
        nom=input("Enter the first name of the trainner you want to edit: ")
        prenom=input("Enter the family name of the trainner you want to edit: ")
        p=-1
        for i in range(n):
            if(nom==t[i].nom and prenom==t[i].prenom):
                p=i
                i=n
        if(p==-1):
            print("Not exes...")
        else:
            t[p].nom=input("Enter the first name of the trainner you want to edit: ")
            t[p].prenom=input("Enter the family name of the trainner you want to edit: ")
            t[p].note1=int(input("Enter note 1:"))
            t[p].note2=int(input("Enter note 2:"))
            t[p].note3=int(input("Enter note 3:"))
    elif(c==3):
        noms=input("Enter the first name of the trainner you want to Del: ")
        prenoms=input("Enter the family name of the trainner you want to Del: ")
        ps=-1
        for i in range(n):
            if(noms==t[i].nom and prenoms==t[i].prenom):
                ps=i
                i=n
        if(ps==-1):
            print("Not exes...")
        else:
            for i in range(ps,n-1):
                t[i]=t[i+1]
            n=n-1
    elif(c==4):
        for i in range(n):
            print(t[i].nom)
            print(t[i].prenom)
            print(t[i].note1)
            print(t[i].note2)
            print(t[i].note3)
    elif(c==5):
        print("Done")
        break
                


            
        
