# ''' Please follow below rules while designing automation script as 

#    * Accept input through command line or through file.
#    * Display any message in log file instead of console.
#    * For separate task define separate function.
#    * For robustness handle every expected exception.
#    * Perform validations before taking any action.
#    * create user defined modules to store the funtionality.

# '''

# ''' 
# 2.Design automation script which accept directory name and write names of duplicate files from that 
# directory into log file named as Log.txt .Log.txt file should be created into current directory.
#     Usage : DirectoryDuplicate.py "Demo"
# Demo is name of directory.
# '''
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

        
def PrintDuplicate(dict1):
    results=list(filter(lambda x:len(x)>1,dict1.values()))

    if(len(results)>0):
        print("Duplicate Found : ")
        print("The following files are identical.")

        icnt=0
        print(results)
        for result in results:
            
            for subresult in result:
                icnt+=1
                if(icnt>=2):
                    print("\t\t%s"%subresult)
                    # print(subresult.split("\\")[:-1])
                    
            icnt=0
    else:
        print("No duplicates found")
        


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
        arr={}
        arr=FindDuplicate(argv[1])
        PrintDuplicate(arr)
        

    except ValueError:
        print("Error : Invalid datatype of input")


if __name__=="__main__":
    main()

# import os
# import hashlib

# def find_duplicate_files(directory):
#     # Dictionary to store file hashes and their corresponding filenames
#     file_hash_dict = {}

#     # List to store duplicate files
#     duplicate_files = []

#     # Iterate through all files in the directory and its subdirectories
#     for root, dirs, files in os.walk(directory):
#         for filename in files:
#             filepath = os.path.join(root, filename)
#             # Calculate the hash of the file
#             with open(filepath, "rb") as file:
#                 file_hash = hashlib.md5(file.read()).hexdigest()
            
#             # Check if the hash is already in the dictionary
#             if file_hash in file_hash_dict:
#                 file_hash_dict[file_hash].append(filepath)
#             else:
#                 file_hash_dict[file_hash] = [filepath]

#     # Filter out file hashes with only one file (no duplicates)
#     for hash_value, files in file_hash_dict.items():
#         if len(files) > 1:
#             duplicate_files.append(files)

#     return duplicate_files

# if __name__ == "__main__":
#     import sys

#     if len(sys.argv) != 2:
#         print("Usage: DirectoryDuplicate.py <directory_name>")
#     else:
#         directory_name = sys.argv[1]
#         if os.path.isdir(directory_name):
#             duplicate_files = find_duplicate_files(directory_name)
#             if duplicate_files:
#                 print("Duplicate files found:")
#                 for duplicate_group in duplicate_files:
#                     print("\n".join(duplicate_group))
#             else:
#                 print("No duplicate files found.")
#         else:
#             print("The specified directory does not exist.")