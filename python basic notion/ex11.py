t=list()
n=int(input("entrer taille de votre class:"))
s=0
for i in range(n):
    print("entrer la notes nemero",i+1,':')
    t.append(int(input()))
    s=s+t[i]
m=s//2
if(m<10):
    print('Non admies')
elif(m<12):
    print("admies")
elif(m<14):
    print("a-bien")
elif(m<16):
    print("bien")
else:
    print("t-bien")
