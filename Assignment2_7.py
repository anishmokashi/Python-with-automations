''' Write a program which accept one number and display below pattern
Input : 5   5
Output :1        2       3       4       5       
        1        2       3       4       5       
        1        2       3       4       5       
        1        2       3       4       5
        1        2       3       4       5


'''
def Pattern(iRow,iCol):
    icnt=1
    for i in range(iRow):
        for j in range(iCol):
            print(icnt,"\t",end=" ")
            icnt=icnt+1
        icnt=1
        print()


def main():
    iNo1=int(input("Enter number of rows "))
    iNo2=int(input("Enter number of columns "))
    Pattern(iNo1,iNo2)

if __name__=="__main__":
    main()