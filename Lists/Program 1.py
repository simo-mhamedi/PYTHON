##created by feecoding

t=list()
n=int(input("Type the size of your list: "))
for i in range(n):
    print("Type the element of the list number ",i+1,":")
    t.append(int(input()))
s=0
for i in range(n):
    s=s+t[i]
print("the sum is = ",s)
