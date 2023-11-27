
def main():
    No = 0
    
    print("Enter number : ")
    No = int(input())

    Result = No % 2

    if(Result == 0):
        print("Number is even")
    else:
        print("Number is odd")

if __name__ == "__main__":
    main()