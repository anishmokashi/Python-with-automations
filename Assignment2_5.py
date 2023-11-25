''' Write a program which accept one number from user and check whether number is prime or not.
Input : 5   Output : Number is prime number

Note : prime number is a number which is divisible by 1 and number itself
'''
def ChkPrime(num):
    ret=True
  
    for i in range(2,int(num/2)+1):
        if(num%i==0):
            ret=False
            break

    return ret

def main():
     iNo1=int(input("Enter number to find if number is prime or not "))
     ret=ChkPrime(iNo1)
     if(ret==True):
         print("Number is a prime number")
     else:
         print("Number is not a prime number")

        
     

if __name__=="__main__":
    main()