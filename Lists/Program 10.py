##created by feecoding

ch=list()
n=int(input("Type the size of your list: "))
for i in range(n):
    print("type a string ",i+1,':')
    ch.append(input())
compt=0
for i in range(n):
    if(ch[i][0]=='A'):
        compt=compt+1
print(compt)
