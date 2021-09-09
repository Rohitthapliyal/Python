n=int(input("enter any number:\n"))
mul=1
while n>0:
    x=n%10
    n=n//10
    mul=mul*x
print(mul)
