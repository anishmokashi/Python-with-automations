'''Write a recursive program which display below pattern
Input : 5 
Output: * * * * *
'''
def RPattern(no):
    # print(no)
    if(no>0):
        print("*")
        # print(no)
        no-=1
        # print(no)
        RPattern(no)
def main():
    RPattern(6)
if __name__=="__main__":
    main()
