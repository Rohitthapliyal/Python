class Add:
    a=int(input("enter  first number:\n"))
    b=int(input("enter second number:\n"))
    def sum(ob):
        ob.c=ob.a+ob.b
    def output(ob):
        print("the sum of two numbers are=",ob.c)

ob1=Add()
ob1.sum()
ob1.output()
