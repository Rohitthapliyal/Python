uc=int(input("enter electrcity unit chargs:\n"))
if uc>=50:
    print(unit*0.50)
elif uc<=150:
    amount=25+(unit-50)*0.75
elif uc<=250:
    amount=100+(unit-50)*1.20
else:
    amount
