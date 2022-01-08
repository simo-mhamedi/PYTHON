##created by feecoding

n=int(input('Enter Your Number:'))
su=0
while(n>0):
    r=n%10
    su=su*10+r
    n=n//10
print(su)
