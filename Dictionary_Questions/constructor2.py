class Tony:
    a=0
    b=0
    c=0
    def __init__(ob):
        ob.a
        ob.b
        
    def show(ob):
        ob.c=ob.a+ob.b
    def output(ob):
        print("sum is=",ob.c)
obj=Tony()
obj.show()
obj.output()
        
