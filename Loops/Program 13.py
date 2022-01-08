##created by feecoding

a=int(input('Enter Your Number :'))
b=a
c=True
for i in range(1,10):
    a=int(input('Enter Your Number :'))
    if(b>a):
        c=False
    b=a
if(c==True):
    print("crouching")
else:
    print("descending")




