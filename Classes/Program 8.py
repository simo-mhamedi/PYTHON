##created by feecoding
class etudient:
    pass
t=list()
n=int(input("Enter Size For Your Liste:"))
for i in range(n):
    t.append(etudient())
    t[i].nom=input("Enter  Name:")
    t[i].age=int(input("Enter Age:"))
    t[i].moyenscolair=float(input("Enter  Your Mean school:"))
s=0
for i in range(n):
    s=s+t[i].age
my=s//n
print("Mean age:",my)
p=0
for i in range(1,n):
    if(t[p].moyenscolair<t[i].moyenscolair):
        p=i
print(t[p].nom)
