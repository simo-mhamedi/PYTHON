##created by feecoding

n=int(input("Input a number: "))
t=list()
for i in range(20):
    print("Input the element of your list: ")
    t.append(int(input()))
compt=0
for i in range(20):
    if(t[i]==n):
        compt=compt+1
print(compt)
