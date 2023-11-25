''' write a program which contains one function that accept one number from user and returns true if 
number is divisible by 5 otherwise return false
Input :8   Output:False
Input :25   Output:True 
 '''
def ChkNum(inum):
    bret=False
    if(inum%5==0):
        bret=True
    return bret


        
def main():
    iNum=int((input("Enter a number")))
    print(ChkNum(iNum))

if __name__=="__main__":
    main()