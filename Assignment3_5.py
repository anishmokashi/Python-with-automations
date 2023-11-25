''' write a program which accept n numbers from user and store it into list.Return addition of all prime numbers from that list.
Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum.
Name of the function from main python file should be ListPrime()

Input :Number of Elements :10
Input Elements : 13 5 45 7 4 56  34 2 5 8
Output : 32(13+5+7+2+5)
'''

from Assignment3_MarvellousNum import ChkPrime 
def ListPrime(List):
    sum=0
    for i in List:
        sum=sum+i
    return sum

def main():
    Numbers=[]
    Size_of_list=int(input("Enter how many elements you want to store in the list"))
    for i in range(Size_of_list):
        numn=int(input())
        if(ChkPrime(numn)):
            Numbers.append(numn)
    print(Numbers)
   
    print("Addition of prime numbers from the entered list is : ",ListPrime(Numbers))


   
    

if __name__=="__main__":
    main()