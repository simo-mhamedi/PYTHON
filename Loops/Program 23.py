##created by feecoding

n=int(input("Enter  Number :"))
test=n
rv=0
while(n>0):
    r=n%10
    rv=rv*10+r
    n=n//10
print(rv)
if(rv==test):
    print("palindrome")
else:
    print("Not palindrome")
