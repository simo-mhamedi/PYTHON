##created by feecoding

def dicision(n):
    if(n<10):
        print("Not success:")
    elif(n<12):
        print("success")
    elif(n>=12):
        print("success With Mention")
t=list()
n=int(input("Enter Size For Your liste:"))
s=0
for i in range(n):
    print("Enter item",i+1,":")
    t.append(int(input()))
    s=s+t[i]
m=s//n
dicision(m)
