''' Write a recursive program which accept number from use and return its factorial.
Input :5
Output :120 
'''
def RFact(num):
    if(num==0 or num==1):
        return 1
    else:
        return(num*(RFact(num-1)))
def main():
    print("Factorial of entered number is : ",RFact(5))

if __name__=="__main__":
    main()
