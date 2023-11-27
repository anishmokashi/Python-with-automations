import sys

def main():
    print("Demonstration of Command line arguments")

    Value1 = int(sys.argv[1])
    Value2 = int(sys.argv[2])
    Ans = Value1 + Value2

    print("Addition is : ",Ans)
        
if __name__ == "__main__":
    main()

# python3 Command1.py 10 11 