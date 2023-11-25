''' Write a program which contains one lambda function which accepts two parameter and return 
its multiplication.
Input : 4   3  output:16
Input : 6   3  output:18

'''
Multiplication=lambda A,B:A*B
def main():
    num1=int(input("Enter number 1 "))
    num2=int(input("Enter number 2 "))
    print("Multiplication of ",num1,"and ",num2,"is",Multiplication(num1,num2))

if __name__=="__main__":
    main()