ph=int(input("enter marks of physics:\n"))
chem=int(input("enter marks of chemistry:\n"))
bio=int(input("enter marks of biology:\n"))
math=int(input("enter marks of mathematics:\n"))
comp=int(input("enter marks of computer:\n"))
per=0
x=(ph+chem+bio+math+comp)
per=(x/500)*100
if per>90:
    print("grade A",per)
elif per>80:
    print("grade B",per)
elif per>70:
    print("grade C",per)
elif per>60:
    print("grade D",per)
elif per>50:
    print("grade E",per)
elif per>40:
    print("grade F",per)

else:
    print("invalid")

