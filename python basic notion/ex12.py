c=0
while(c!=4):
    print("1:pour la surface:")
    print("2:pour la pirmetre d'un cercal:")
    print("3:pour volume cylinder:")
    print("4:poour quitter")
    c=int(input())
    if(c==1):
      r=float(input("entrer le reyome:"))
      surface=r*r*3.14
      print(surface)
    elif(c==2):
      r=float(input("entrer le reyome:"))
      perm=(2*3.14*r)
      print(perm)
    elif(c==3):
       r=float(input("entrer le reyome:"))
       h=float(input("entrer le H:"))
       v=(r*r*3.14*h)
       print(v)
    else:
        print('fin')