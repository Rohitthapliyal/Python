import math
class Power:
    x=int(input("enter any number:\n"))
    y=int(input("enter base:\n"))
    def show(ob):
       ob.power=math.pow(ob.x*ob.y)
    def output(ob):
        print("power of the number is=",ob.power)
obj=Power()
obj.show()
obj.output()
        
