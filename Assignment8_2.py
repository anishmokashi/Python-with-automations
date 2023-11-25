'''Write a recursive program which display below pattern
Input : 5 
Output: 1 2 3 4 5 
'''
i=1
def RPattern(no):
    # print(no)
    global i
    if(i<=no):
        print(i,end=" ")
        # print(no)
        i+=1
        
        # print(no)
        RPattern(no)
def main():
    RPattern(5)
if __name__=="__main__":
    main()
