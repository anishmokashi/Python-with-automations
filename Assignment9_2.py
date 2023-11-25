''' Write a program which accept file name from user and open that file and display the contents of that file on screen
Input :Demo.txt
Display contents of Demo.txt on console'''

import os
def main():
    File_name=input("Enter the file name ")
    
    if os.path.exists(File_name):
        fobj=open(File_name,"r")
        if fobj:
            print("File successfully opened in reading mode")
           
            Data=fobj.read()
            print("Data from file is : ",Data)
            fobj.close()
        else:
            print("Unable to open file")
    else:
        print("There is no such file")
if __name__=="__main__":
    main()