class Arithematic:
    def __init__(self,A,B):
        print("Inside constructor")
        self.No1 = A
        self.No2 = B

    def Addition(self):
        Ans = 0
        Ans = self.No1+self.No2
        return Ans

    def Substraction(self):
        Ans = 0
        Ans = self.No1-self.No2
        return Ans

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    
    obj1 = Arithematic(Value1,Value2)
    
    Ret = obj1.Addition()
    print("Addition is : ",Ret)
    
    Ret = obj1.Substraction()
    print("Substraction is : ",Ret)

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    
    obj2 = Arithematic(Value1,Value2)
    
    Ret = obj2.Addition()
    print("Addition is : ",Ret)
    
    Ret = obj2.Substraction()
    print("Substraction is : ",Ret)

if __name__ == "__main__":
    main()