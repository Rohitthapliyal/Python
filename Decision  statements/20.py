bs=int(input("enter basic salary of an employee:\n"))
if bs>=10000:
    HRA=bs*20/100
    print(HRA)
    DA=bs*80/100
    print(DA)
    grosssalary=HRA+DA
    print(grosssalary)
elif bs>=20000:
    HRA=bs*25/100
    print(HRA)
    DA=bs*90/100
    print(DA)
    grosssalary=HRA+DA
    print(grosssalary)
elif bs>=30000:
    HRA=bs*30/100
    print(HRA)
    DA=bs*95/100
    print(DA)
    grosssalary=HRA+DA
    print(grosssalary)
else:
    print("invalid")
