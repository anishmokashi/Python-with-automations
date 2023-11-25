''' Please follow below rules while designing automation script as 

   * Accept input through command line or through file.
   * Display any message in log file instead of console.
   * For separate task define separate function.
   * For robustness handle every expected exception.
   * Perform validations before taking any action.
   * create user defined modules to store the funtionality.

'''

''' 
1.Design automation script which accept directory name and display checksum of all files.
    Usage : DirectoryChecksum.py "Demo"
Demo is name of directory.
'''
from sys import *
import os
import hashlib
def hashfile(path,blocksize=1024):
    afile=open(path,"rb")
    hasher=hashlib.md5()
    buf=afile.read(blocksize)
    while( len(buf)>0):
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def Display_CheckSum_of_all_files_in_a_folder(path):
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)
    if exists:
        for dirname,subdir,filelist in os.walk(path):
            print("Current folder is : "+dirname)
            for filen in filelist:
                path=os.path.join(dirname,filen)
                file_hash=hashfile(path)
                print(filen,"named file on path : ",path)
                print("And its Check sum is :",file_hash)
                print(" ")
    
    
    
    
    
    


def main():
    print("----------------Display Checksum--------------")
    print("Application name: "+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and display checksum of files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory Extentsion")
        exit()

    
    
    try:
        Display_CheckSum_of_all_files_in_a_folder(argv[1])
        
        

    except ValueError:
        print("Error : Invalid datatype of input")


if __name__=="__main__":
    main()