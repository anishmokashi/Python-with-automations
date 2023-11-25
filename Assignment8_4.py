''' Wrote a recursive program which accept number from user and return summation of its digits.
Input : 879 
Output : 24
'''
def Summation_of_digits(num):
    sum=0
    digit=0
    while(num!=0):
        digit=num%10
        sum=sum+digit
        num=num//10
    return sum
def main():
    print("Summation of entered digits is :",Summation_of_digits(879))

if __name__=="__main__":
    main()