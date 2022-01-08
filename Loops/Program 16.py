##created by feecoding

n=int(input('Enter Your Number:'))
b=True
for i in range(2,n+1//2):
    if(n%i==0):
        b=False
if(b==True):
    print("First")
else:
    print("Not First")
