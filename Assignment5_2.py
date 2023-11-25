''' Write a program which contains one class named as Circle.
Circle class contains three instance variables as Radius ,Area,Circumference.
That class contains one class variable as PI which is initialise to 3.14.
Inside init method initialise all instance variables to 0.0.
There are three instance methods inside class as Accept(),CalculateArea(),
CalculateCircumference(),Display().
Accept method will accept value of radius from user.
CalculateArea() method will calculate area of circle and store it into instance variable Area.
CalculateCircumference() method will calculate circumference of circle and store it into instance
variable Circumference.
And Display() method will display value of all the instance variables as Radius,Area,Circumference.
After designing the above class call all instance methods by creating multiple objects.

'''
class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0
    def Accept(self):
        self.Radius=int(input("Enter radius : "))
    def CalculateArea(self):
        self.Area=Circle.PI *(self.Radius**2) 
    def CalculateCircumference(self):
        self.Circumference=2*self.PI*self.Radius

    def Display(self):
        print("Radius of circle is : ",self.Radius)
        print("Area of circle is : ",self.Area)
        print("Circumference of circle is : ",self.Circumference)

def main():
    print("First object")
    print()
    Obj1=Circle()
    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()
    print()
    print()
    print("Second object")
    print()
    Obj2=Circle()
    Obj2.Accept()
    Obj2.CalculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()

if __name__=="__main__":
    main()

