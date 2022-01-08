##created by feecoding

def somme(n):
    if(n==0):
        return 0
    else:
        return n+somme(n-1)
n=int(input("type the number: "))
print(somme(n))
