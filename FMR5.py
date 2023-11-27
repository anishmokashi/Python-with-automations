from functools import reduce

CheckEven = lambda No: (No % 2 == 0)

Increase = lambda No: No+2

Add = lambda A,B: A+B

def main():
    Data = []

    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    
    print("Input data : ",Data)
    
    output = list(filter(CheckEven,Data))
    print("Output after filter : ",output)

    moutput = list(map(Increase,output))
    print("Output after map : ",moutput)

    result = reduce(Add,moutput)
    print("Output after reduce : ",result)

if __name__ == "__main__":
    main()