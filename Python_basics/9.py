import math 
class Circle:
    r=int(input("enter radius:\n"))
    diameter=0
    circumference=0
    area=0
    def ron(ob):
        ob.diameter=2*ob.r
        ob.circumference=2*math.pi*ob.r
        ob.area=math.pi*ob.r*ob.r
        
    def output(ob):
        print("diameter of circle is=",ob.diameter)
        print("circumference of circle is=",ob.circumference)
        print("area of circle is=",ob.area)
ob1=Circle()
ob1.ron()
ob1.output()
