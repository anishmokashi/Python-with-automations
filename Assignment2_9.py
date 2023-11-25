''' write a program which accept one number from user and return number of digits in that number
Input : 5187934  Output : 7

'''

def CountDigits(num):

    icnt=0
    print(num)
    while(num!=0):
        icnt=icnt+1
        
        num=num//10
    
    return icnt


def main():
    iNo1=int(input("Enter number"))
    
    print("Number of digits present in the number are",CountDigits(iNo1))

if __name__=="__main__":
    main()