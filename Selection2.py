def CheckEven(Value):
    Result = Value % 2

    if(Result == 0):
        print("Number is even")
    else:
        print("Number is odd")

def main():    
    print("Enter number : ")
    No = int(input())

    CheckEven(No)

if __name__ == "__main__":
    main()