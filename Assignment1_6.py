''' write a program which accept number from user and check whether that number is positive or negative or zero
Input :11   Output:Positive number
Input :-8   Output:Negative number 
Input :0   Output:Zero '''
def ChkNum(inum):
    if(inum==0):
        print("Zero")
    elif(inum<0):
        print("Negative number")
    else:
        print("positive number")


        
def main():
    iNum=int((input("Enter a number")))
    ChkNum(iNum)

if __name__=="__main__":
    main()