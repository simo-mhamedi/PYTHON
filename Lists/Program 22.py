##created by feecoding

t=list()
for i in range(4):
    t.append(list())
    for j in range(5):
        print("Enter item :")
        t[i].append(int(input()))
l=4
c=5
for j in range(c):
    d=0
    for i in range(l):
        if(t[i][j]%3==0):
            d=d+1
    print("For Line:",j+1,':',d)
    if(j==3):
        j=5

for i in range(l):
    r=0
    for j in range(c):
        if(t[i][j-1]%3==0):
            r=r+1
    print("For Culome:",i+1,':',r)
    if(i==3):
        l=l+1
s=0
for i in range(4):
    for j in range(5):
        if(t[i][j]%3==0):
            s=s+1
print(s)
    
