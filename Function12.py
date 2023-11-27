
# Function defines another function inside it (Inner Function)
def Demo(Value1,Value2):
    def Add(A, B):  
        return A+B

    Ans = Add(Value1,Value2)
    return Ans

def main():
    Ret = Demo(11,7) 
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()