#created by feecoding

n=int(input("enter the number of the first item:"))
total=0
for i in range(1,n+1):
    print("enter the price of the product",i,':')
    price=float(input())
    total=total+price
somme=float(input("enter the sum: "))
fp=somme-total
print("made:",fp)
