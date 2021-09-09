n=int(input("enter any number:\n"))
sum=0
for i in range(1,n):
    if i%3==0:
        sum=sum+i
        print(sum)
