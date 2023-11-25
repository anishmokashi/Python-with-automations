# write a program which contains one function named as ChkNum which accept one parameter as number.
# If number is even then it should display "Even number" otherwise display "odd number" on console.
# Input :11   Output:Odd number
# Input :8   Output:Even number

def ChkNum(inum):
    if((inum%2)==0):
        print("Even number")
    else:
        print("Odd number")
def main():
    iNum=int((input("Enter a number")))
    ChkNum(iNum)

if __name__=="__main__":
    main()