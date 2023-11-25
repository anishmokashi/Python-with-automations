''' write a program which accept one number from user and return addition of digits in that number
Input : 5187934  Output : 37

'''

def AddDigits(num):
    iDigit=0
    icnt=0
    print(num)
    while(num!=0):
        iDigit=num%10
        icnt=icnt+iDigit
        
        num=num//10
    
    return icnt


def main():
    iNo1=int(input("Enter number"))
    
    print("Addition of digits present in the number are",AddDigits(iNo1))

if __name__=="__main__":
    main()