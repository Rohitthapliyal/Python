#class Ron:
    #def init(self):
        #self.greek="rohitthapliyal"

    #def sam(self):
        #print("welcome")
#obj=Ron()
#obj.sam()



class Addition:
    first=0
    second=0
    answer=0
    
    def __init__(self,m,n):
        self.first=m
        self.second=n
    def display(self):
        print("first number=",self.first)
        print("second number=",self.second)
        print("addition of two numbers are=",self.answer)
    def calculate(self):
        self.answer=self.first+self.second
obj=Addition(500,600)
obj.calculate()
obj.display()
