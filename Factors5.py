
def DisplayFactors(Value):
    i = 1
    while(i < Value):
        if(Value % i == 0):
            print(i)
        i = i + 1

def main():
    No = 0
    print("Enter number")
    No = int(input())
    DisplayFactors(No)

if __name__ == "__main__":
    main()
