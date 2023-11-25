'''Write a recursive program which display below pattern
Input : 5 
Output: 5 4 3 2 1 
'''
def RPattern(no):
    # print(no)
    
    if(no>0):
        print(no,end=" ")
        # print(no)
        no-=1
        
        # print(no)
        RPattern(no)
def main():
    RPattern(5)
if __name__=="__main__":
    main()
