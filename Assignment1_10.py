''' write a program which accept name from user and display length of its name.
Input : Marvellous          Output: 10
 '''
def PrintStr(string):
    count=0
    for i in string:
        count=count+1
    print("Length of string is ",count)


        
def main():
    Str=(input("Enter a string : "))
    PrintStr(Str)

if __name__=="__main__":
    main()