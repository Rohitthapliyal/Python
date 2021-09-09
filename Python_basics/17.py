class Triangle:
    base=int(input("enter base of triangle:\n"))
    height=int(input("enter height of triangle:\n"))
    def show(ob):
        ob.area=1/2*ob.base*ob.height
    def output(ob):
        print("area of triangle is=",ob.area)
obj=Triangle()
obj.show()
obj.output()
