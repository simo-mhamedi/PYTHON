##created by feecoding

a=int(input("Enter Your First Number: "))
b=a
for i in range(1,10):
    a=int(input("Enter Your Second Number: "))
    if(b<a):
        b=a
print(b)
