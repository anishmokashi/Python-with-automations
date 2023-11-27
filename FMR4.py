# Unnamed Function (lambda function / Anonymous Function)
# Name = lambda Parameters_List : Functions_Logic

def Add(No1,No2):
    return No1 + No2

AddX = lambda No1,No2 :  No1 + No2

def CheckEven(No):
    return (No % 2 == 0)

CheckEvenX = lambda No: (No % 2 == 0)

def Increase(No):
    return No + 2

IncreaseX = lambda No: (No + 2)

def main():
    Ret = Add(10,11)
    print(Ret)
    Ret = CheckEven(10)
    print(Ret)
    Ret = Increase(10)
    print(Ret)

    Ret = AddX(10,11)
    print(Ret)
    Ret = CheckEvenX(10)
    print(Ret)
    Ret = IncreaseX(10)
    print(Ret)

if __name__ == "__main__":
    main()