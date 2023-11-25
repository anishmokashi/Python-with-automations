''' Accept file name and one string from user and return the frequency of that string from file.
Input : Demo.txt Marvellous
search "Marvellous" in Demo.txt
'''
import sys
def count_Freq_of_str(f1):
    
    str=input("Enter the string of which frequency you want to count ")
    str_count=0
    f1obj=open(f1,"r")
    file_read=f1obj.read()
    
    if str in file_read :
        str_count+=1
    f1obj.close()
    print("Count of ",str," in ",f1," is ",str_count)


def main():
    file_name=sys.argv[1]
    print("You have entered file name through commandline argument")
    count_Freq_of_str(file_name)


if __name__=="__main__":
    main()