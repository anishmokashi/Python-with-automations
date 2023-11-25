# ''' Please follow below rules while designing automation script as 

#    * Accept input through command line or through file.
#    * Display any message in log file instead of console.
#    * For separate task define separate function.
#    * For robustness handle every expected exception.
#    * Perform validations before taking any action.
#    * create user defined modules to store the funtionality.

# '''

''' 
4.Design automation script which accept directory name and delete all duplicate files from that directory. 
Write Names of duplicate files from that directory into log file named as Log.txt.
Log.txt file should be created into current directory.Display execution time required for the script.

    Usage : DirectoryDuplicateRemoval.py"Demo"

Demo is name of directory.
'''
from sys import *
import os
import hashlib
import time
def hashfile(path,blocksize=1024):
    afile=open(path,"rb")
    hasher=hashlib.md5()

    buf=afile.read(blocksize)
    while( len(buf)>0):
        hasher.update(buf)
        buf=afile.read(blocksize)

    afile.close()

    return hasher.hexdigest()

def FindDuplicate(path):
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)
    exists=os.path.isdir(path)

    file_hash_dict = {}
   
    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            
            for filen in fileList:
               
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                if file_hash in file_hash_dict:
                    file_hash_dict[file_hash].append(path)
                else:
                    file_hash_dict[file_hash] = [path]

        return file_hash_dict
    else :
        print("Invalid Path")

        
def Delete_Duplicate(dict1):
    
    separator="-"*100
    filename="DeletedFileslog.txt"
    filename=os.path.abspath(filename)
   
    fd=open(filename,"w")
    fd.write(separator+"\n")
    fd.write("Deleted Duplicate files Logger Generated at "+"\t"+time.ctime()+"\n")
    fd.write(separator+"\n")

    results=list(filter(lambda x:len(x)>1,dict1.values()))
    
    icnt=0
    if(len(results)>0):
        
        fd.write("Files Deleted are : \n")

        
       
        for result in results:
            
            for subresult in result:
                icnt+=1
                if(icnt>=2):
                    
                    
                    fd.write("\t%s\n"%subresult)
                    os.remove(subresult)
                    
                    
            icnt=0
    else:
        fd.write("No duplicates found")
        


def main():
    print("----------------Duplicate file deletion--------------")
    print("Application name: "+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and delete duplicate files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName foldername")
        exit()

    
    
    try:
        arr={}
        Starttime=time.time()
        arr=FindDuplicate(argv[1])
        Delete_Duplicate(arr)
        Endtime=time.time()
        print("Time taken to execute the script is %s",Starttime-Endtime)
        

    except ValueError:
        print("Error : Invalid datatype of input")


if __name__=="__main__":
    main()