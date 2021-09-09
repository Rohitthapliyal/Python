class Add:
    a=int(input("enter first no:\n"))
    b=int(input("enter second no:\n"))
    def sum(ob):
        ob.a+=ob.b
    def output(ob):
        print("the sum of two numbers is=",ob.a)
ob1=Add()
ob1.sum()
ob1.output()
