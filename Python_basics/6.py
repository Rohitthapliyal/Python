class Arith:
    a=int(input("enter first number:\n"))
    b=int(input("enter second number:\n"))
    def opr(obj):
        obj.add=obj.a+obj.b
        obj.subtract=obj.a-obj.b
        obj.divide=obj.a/obj.b
        obj.multiply=obj.a*obj.b
    def output(obj):
        print("addition=",obj.add)
        print("subtract=",obj.subtract)
        print("division=",obj.divide)
        print("multiply=",obj.multiply)
obj1=Arith()
obj1.opr()
obj1.output()
