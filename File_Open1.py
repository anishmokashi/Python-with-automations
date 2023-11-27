import os

def main():
    print("Enter the name of file that you want to open for reading purpose : ")
    File_name = input()

    if os.path.exists(File_name):
        fobj = open(File_name,"r")
        if fobj:
            print("File succesfully opened")
            fobj.close()
        else:
            print("Unable to open file")
    else: 
        print("There is no such file")

if __name__ == "__main__":
    main()