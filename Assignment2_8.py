''' Write a program which accept one number and display below pattern
Input : 5   
Output :1        
        1        2       
        1        2       3       
        1        2       3       4       
        1        2       3       4       5       


'''
def Pattern(iRow):
    icnt=1
    for i in range(iRow):
        for j in range(i+1):
            print(icnt,"\t",end=" ")
            icnt=icnt+1
        icnt=1
        print()


def main():
    iNo1=int(input("Enter number"))
    
    Pattern(iNo1)

if __name__=="__main__":
    main()