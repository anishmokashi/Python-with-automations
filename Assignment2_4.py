''' Write a program which accept one number from user and return addition of its factors.
Input : 12   Output : 16 (1+2+3+4+6)
'''
def AddFactors(num):
    addition_of_factors=0
  
    for i in range(1,num):
       
        if(num%i==0):
            
            addition_of_factors=addition_of_factors+i

    return addition_of_factors

def main():
     iNo1=int(input("Enter number to find addition of its factors "))
     print("Addition of factors of ",iNo1,"is ",AddFactors(iNo1))


if __name__=="__main__":
    main()