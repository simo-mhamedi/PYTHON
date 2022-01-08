##created by feecoding

ch=list()
for i in range(5):
    print("Type a string ",i+1,':')
    ch.append(input())
ch2=list()
for i in range(5):
    for j in reversed(ch[i]):
        ch2.append(j)
print(ch2)
