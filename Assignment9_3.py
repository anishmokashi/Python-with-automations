'''Write a program which accept file name from user and create new file named as Demo.txt and
copy all contents from existing file into new file.Accept file name through command line arguments 
Input : ABC.txt'''
import os
import sys
def main():
    print("You have entered data through commandline ")
    Dest_file=sys.argv[1]
    File_name=input("Enter the file name from which you want to transfer data ")
    fobj1=open(File_name,"r")#open file in read mode
    fobj2=open(Dest_file,"a")#open file in append mode
    if (os.path.exists(File_name)):
        
        if fobj1:
            F1_read=fobj1.read()
            fobj2.write(F1_read)
            print("Data copied from ",File_name," to ",Dest_file)
            fobj1.close()
            fobj2.close()
            y_n=input("Press y if you want to see the copied data from the source file to dest file")
            if(y_n=="y" or y_n=="Y"):
                fobj2=open(Dest_file,"r")
                print(fobj2.read())

        else:
            print("File dosent exist")
    else:
        print("Unable to open file")
if __name__=="__main__":
    main()