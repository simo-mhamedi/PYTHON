##created by feecoding

ch=input("Enter your string for test:")
c=len(ch)-1
b=True
for i in range(c//2):
    if(ch[i]!=ch[c-i]):
        b=False
if(b==True):
    print("palindrome")
else:
    print("Not palindrome")
