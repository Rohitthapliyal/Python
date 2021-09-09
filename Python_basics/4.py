class Swap2:
    a=int(input("enter first number:\n"))
    b=int(input("enter second number:\n"))
    def show(ob):
        ob.a=ob.a+ob.b
        ob.b=ob.a-ob.b
        ob.a=ob.a-ob.b
    def output(ob):
        print("after swapping:\n")
        print("first number=",ob.a,"second number=",ob.b)
ob1=Swap2()
ob1.show()
ob1.output()
