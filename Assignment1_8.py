''' write a program which accepts number from user and print that number of " * " on screen.
Input :5   Output: *       *       *       *       * 
 '''
def PrintNum(inum):
    for i in range(0,inum):
        print("\t*",end=" ")


        
def main():
    iNum=int((input("Enter a number")))
    PrintNum(iNum)

if __name__=="__main__":
    main()