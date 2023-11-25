''' Write a program which accept one number and display below pattern
Input : 5   
Output :*        *       *       *       *
        *        *       *       *
        *        *       *
        *        *
        *


'''
def Pattern(iRow):
    for i in range(iRow):
        for j in range(iRow-i):
            print("*\t",end=" ")
        print()


def main():
    iNo1=int(input("Enter number"))
    
    Pattern(iNo1)

if __name__=="__main__":
    main()