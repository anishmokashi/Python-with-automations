''' Write a program which accept one number from user and return its factorial.
Input : 5   Output : 120
'''
def Factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact=fact * i
    return fact

def RFactorial(num):
    if ((num==0)or(num==1)):
        return 1
    else:
        return num * RFactorial(num-1)
def main():
     iNo1=int(input("Enter number to find factorial "))
     print("Factorial of ",iNo1,"without recursion is ",Factorial(iNo1))
     print("Factorial of ",iNo1,"with recursion is ",RFactorial(iNo1))


if __name__=="__main__":
    main()