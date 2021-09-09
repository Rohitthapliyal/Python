class Swap:
    a=int(input("enter first number:\n"))
    b=int(input("enter second number:\n"))
    def show(ob):
        print("values before swapping:\n",ob.a,ob.b)
        ob.c=ob.a
        ob.a=ob.b
        ob.b=ob.c
        #print("values before swapping:\n",ob.a,ob.b)
    def output(ob):
        print("values after swapping are:\n")
        print("first number",ob.a,"second number",ob.b)
ob1=Swap()
ob1.show()
ob1.output() 
