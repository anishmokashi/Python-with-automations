''' Write a program which accept two file names from user and compare contents of both the files.
If both the files contains same contents then display success otherwise display failure.
Accept names of both the files from command line.

Input : Demo.txt Hello.txt
Compare contents of Demo.txt and Hello.txt
'''
import filecmp

def main():
    f1=input("Enter the name of first file ")
    f2=input("Enter the name of second file ")
    if(filecmp.cmp(f1,f2,shallow=False)):#shallow copy false means we are comparing deep copy means the acutal data from both the files
        print("Success")
    else:
        print("Failure")



if __name__=="__main__":
    main()
