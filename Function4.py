
# Function accepts  parameter and return parameter
def Marvellous(Value1, Value2):
    if(Value1 > Value2):
        return Value1
    else:
        return Value2

def main():
    Ret = Marvellous(78,45)
    print("Largest number is : ",Ret)

    Ret = Marvellous(34,99)
    print("Largest number is : ",Ret)

if __name__ == "__main__":
    main()