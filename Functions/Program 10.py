##created by feecoding

def u(n):
    if(n==0):
        return 1
    else:
        return 2+3*u(n-1)
n=int(input('input:'))
print(u(n))
