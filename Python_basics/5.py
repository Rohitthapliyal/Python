class Average:
    a=int(input("enter first number:\n"))
    b=int(input("enter second number:\n"))
    c=int(input("enter third number:\n"))
    av=float()
    def avg(obj):
        obj.av=(obj.a+obj.b+obj.c)//3
    def output(obj):
        print("average of three varaibles are=",obj.av)
obj1=Average()
obj1.avg()
obj1.output()
