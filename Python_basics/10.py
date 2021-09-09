class Ron:
    l=int(input("enter lenght in cm:\n"))
    def show(obj):
        obj.meter=obj.l/100.0
        obj.kilometer=obj.l/1000.0
    def output(obj):
        print("length in meter is=",obj.meter)
        print("length in kilometer is=",obj.kilometer)
obj1=Ron()
obj1.show()
obj1.output

