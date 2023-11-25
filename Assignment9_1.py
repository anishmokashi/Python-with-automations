''' Write a program which accepts file name from user and check whether that file exists in current directory or not 
Input : Demo.txt
Check whether Demo.txt exists or not'''
import os

def main():
    print("Please enter the file name that you want to check if it is present in the current directory ") 
    File_name=input()

    if os.path.exists(File_name):
        print("File exists")
    else:
        print("File dosent exits")
if __name__=="__main__":
    main()