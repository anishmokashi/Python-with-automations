''' Create a module named as Arithmetic which contains 4 functions as Add() for addition,
Sub() for substraction , Mult for multiplication and Div() for division . All functions 
accepts two paraameters as number and perform the operation . Write a python program which will call all the functions 
from arithmetic module by accepting the parameters from user.
'''
import Assignment2_Arithmetic
def main():
    iNo1=int(input("Enter first number "))
    iNo2=int(input("Enter second number "))

    Matchparam=int(input("Enter \n 1. For Addition \n 2. For Substraction\n 3. For Multiplication \n 4. For Division \n "))
    match Matchparam:
        case 1:
            print("Addition of",iNo1,"and",iNo2,"is : ",Assignment2_Arithmetic.Add(iNo1,iNo2))
        case 2:
            print("Substraction of",iNo1,"and",iNo2,"is : ",Assignment2_Arithmetic.Sub(iNo1,iNo2))
        case 3:
            print("Multiplication of",iNo1,"and",iNo2,"is : ",Assignment2_Arithmetic.Mult(iNo1,iNo2))
        case 4:
            print("Division of",iNo1,"and",iNo2,"is : ",Assignment2_Arithmetic.Div(iNo1,iNo2))
        case _ :
            print("Please enter valid inputs")
if __name__=="__main__":
    main()