class Shape:
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width  = width
    def area(self):
        print(self.length * self.width)
class rectangle(Shape):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        print(self.length*self.width)

length, width = map(int,input().split())
myRectangle=rectangle(length=length,width=width)
myRectangle.area()