##created by feecoding

c=0
while(c!=4):
    print("1:for surface")
    print("2:for the perimeter of a circle")
    print("3:for cylinder volume")
    print("4:Quit")
    c=int(input())
    if(c==1):
      r=float(input("Type the raduis: "))
      surface=r*r*3.14
      print(surface)
    elif(c==2):
      r=float(input("Type the radius: "))
      perm=(2*3.14*r)
      print(perm)
    elif(c==3):
       r=float(input("Type the radius: "))
       h=float(input("Type the height: "))
       v=(r*r*3.14*h)
       print(v)
    else:
        print('fin')
