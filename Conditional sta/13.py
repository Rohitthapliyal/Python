n=int(input("enter any number:\n"))
sum=0
while n>0:
    x=n%10
    n=n//10
    sum=sum+x
print(sum)
