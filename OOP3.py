class Demo:
    def __init__(self, Value1, Value2):     # Constructor
        print("Inside init method")
        self.No1 = Value1
        self.No2 = Value2

    def Display(self):
        print("Value of No1 : ",self.No1)
        print("Value of No2 : ",self.No2)

def Starter():
    print("Demonstration of Object Orientation")

    obj1 = Demo(10,20)  # __init__(100,10,20)
    obj2 = Demo(11,21)  # __init__(200,11,21)

    obj1.Display()  # Display(100)
    obj2.Display()  # Display(200)

if __name__ == "__main__":
    Starter()