class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def display(self):
        return self.height*self.width

height=int(input("Enter The Height of Rectangle::"))
width=int(input("Enter The Width of Rectangle::"))
obj=Rectangle(height,width)
print("The Area Of Rectangle::",obj.display())
