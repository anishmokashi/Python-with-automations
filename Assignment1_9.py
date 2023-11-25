''' Write a program which display first 10 even numbers on screen
Output : 2 4 6 8 10 12 14 16 18 20 
'''

# def ChkNum(inum):
#     i=1
#     while(i<=inum):
#         if(i%2==0):
#             print(i,end=" ")
#         i=i+1
# def main():
#     iNum=int((input("Enter a number")))
#     ChkNum(iNum)

# if __name__=="__main__":
#     main()

def checkNum():
  
    i=1
    icount=0
    while(1):
        if(i%2==0):
            print(i)
            icount=icount+1
            
        elif(icount==10):
            break
        i=i+1
        
        


def main():
    
    checkNum()


if __name__=="__main__":
    main()