class Method:
    def __init__(self):
        self.string=""
    def get(self):
        self.string=input("Enter the String::")
    def put(self):
        print(self.string)
obj=Method()
obj.get()
obj.put()
