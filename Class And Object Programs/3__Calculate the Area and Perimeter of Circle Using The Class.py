import math
class  Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
radius=int(input("Enter The Radius Of Circle::"))
obj=Circle(radius)
print("Area Of Circle::",round(obj.area(),2))
print("Perimeter of Circle::",round(obj.perimeter(),2))
