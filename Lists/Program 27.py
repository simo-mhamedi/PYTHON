##created by feecoding

ch=list()
n=int(input("Enter Size For Your liste:"))
for i in range(n):
    print("Enter string",i+1,':')
    ch.append(input())
p=int(input("Enter position For delet..... it:"))
del ch[p]
print(ch)
