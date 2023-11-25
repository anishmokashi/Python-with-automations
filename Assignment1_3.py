# write a program which contains one function named as Add() which accept two numbers from user and return addition of that two numbers.
# Input :11 5  Output:16


def Add(inum1,inum2):
    return inum1+inum2
def main():
    iNum1=int((input("Enter first number :")))
    iNum2=int((input("Enter second number :")))
    print("Addition of two numbers is:",Add(iNum1,iNum2))

if __name__=="__main__":
    main()