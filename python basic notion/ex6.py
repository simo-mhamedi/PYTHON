n=int(input("entrer la nomber de predui:"))
total=0
for i in range(1,n+1):
    print("entrer prix de preduit",i,':')
    prix=float(input())
    total=total+prix
somme=float(input("enter votre somme:"))
rendu=somme-total
print("rendu ci:",rendu)
