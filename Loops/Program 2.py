##created by feecoding

t=list()
n=int(input("enter your class size: "))
s=0
for i in range(n):
    print("enter degree number ",i+1,':')
    t.append(int(input()))
    s=s+t[i]
m=s//2
if(m<10):
    print('Not admitted')
elif(m<12):
    print("admitted")
elif(m<14):
    print("good")
elif(m<16):
    print("amazing")
else:
    print("perfect job")
