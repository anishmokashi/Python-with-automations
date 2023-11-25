''' write a program which contains one class named as Arithmetic .
Arithmetiv vlass contains three instance variables as Value1 Value2.
Inside init method initialise all instance variables to 0
There are three instance methods inside class as Accept(),Addition(),Substraction(),
Multiplication(),Division().
Method will accept value of value2 and value2 from user.
Addition() method will perform addition of value1 and value2 and return result.
Substraction() method will perform Substraction of value1 and value2 and return result.
Division() method will perform Division of value1 and value2 and return result.
After designing the above class call all instance methods by creating multiple objects
'''
class Artithmetic:
    def __init__(self):
        self.Value1=0
        self.Value2=0
    def Accept(self):
        self.Value1=int(input("Enter first number : "))
        self.Value2=int(input("Enter second number : "))
    def Addition(self):
        return self.Value1 + self.Value2
    def Substraction(self):
        return self.Value1 - self.Value2
    def Multiplication(self):
        return self.Value1 * self.Value2
    def Division(self):
        return self.Value1 / self.Value2
def main():
    print("First object")
    Obj1=Artithmetic()
    Obj1.Accept()
    print("Addition of two numbers is ",Obj1.Addition())
    print("Substraction of two numbers is ",Obj1.Substraction())
    print("Multiplication of two numbers is ",Obj1.Multiplication())
    print("Division of two numbers is ",Obj1.Division())
    print()
    print()
    Obj2=Artithmetic()
    Obj2.Accept()
    print("Addition of two numbers is ",Obj2.Addition())
    print("Substraction of two numbers is ",Obj2.Substraction())
    print("Multiplication of two numbers is ",Obj2.Multiplication())
    print("Division of two numbers is ",Obj2.Division())
if __name__=="__main__":
    main()
    