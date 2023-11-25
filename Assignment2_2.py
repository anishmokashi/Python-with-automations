''' write a program which accept one number and display below pattern 
Input : 5

Output :*        *       *       *       *
        *        *       *       *       *
        *        *       *       *       *
        *        *       *       *       *
        *        *       *       *       *
'''
def Pattern(iRow,iCol):
    for i in range(iRow):
        for j in range(iCol):
            print("*\t",end=" ")
        print()


def main():
    iNo1=int(input("Enter number of rows "))
    iNo2=int(input("Enter number of columns "))
    Pattern(iNo1,iNo2)

if __name__=="__main__":
    main()