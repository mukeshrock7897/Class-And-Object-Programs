class Check:
    def __init__(self):
        self.n=[]
    def add(self,a):
        return self.n.append(a)
    def remove(self,b):
        return  self.n.remove(b)
    def dis(self):
        return self.n
obj=Check()

choice=1
while choice!=0:
    print("0--Exit")
    print("1--Add")
    print("2--Delete")
    print("3--Display")
    choice=int(input("Enter the Choice::"))
    if choice==1:
        n=int(input("Enter  Element To Append::"))
        print(obj.add(n))
    elif choice==2:
        n=int(input("Enter The Element For Remove"))
        print(obj.remove(n))
    elif choice==3:
        print("displayed The All Avaible Element")
        print(obj.dis())
    elif choice==0:
        print("Exiting")
    else:
        print("Invalid Choice")
print()
