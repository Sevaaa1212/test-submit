#class类 18and19课
class Calculator:
    #属性
    name = 'Good calculator'
    price = 18

    def __init__(self,name,price,height=12,width,weight):
        self.name = name
        self.price = price
        self.h = height
        self.w = width
        self.we = weight
    #功能
    def add(self,x,y):
        result = x+y
        print(self.name,result)#类内调用自己self.xx

    def minus(self,x,y):
        result = x-y
        print(result)

    def times(self,x,y):
        result = x*y
        print(result)

    def divide(self,x,y):
        print(x/y)

    
