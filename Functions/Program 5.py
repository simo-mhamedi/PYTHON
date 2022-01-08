##created by feecoding

def afficher(t,n):
    for i in range(n):
        print(t[i])
n=int(input("Type the size of your list: "))
t=list()
for i in range(n):
    print("enter the elements of the list: ")
    t.append(int(input()))
afficher(t,n)
