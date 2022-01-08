##created by feecoding

while True:
    a=int(input("Enter Your First Number:"))
    b=int(input("Enter Your Second Number:"))
    print("s:For sum")
    print("m:For Multy")
    print("d:For Deferent")
    print("q:For To leave")
    c=input()
    if(c=='s'):
        r=a+b
        print("sum:",r)
    elif(c=='p'):
        r=a*b
        print("Multy",r)
    elif(c=='d'):
        r=a-b
        print("Deferent:",r)
    else:
        print("Done")
        break
