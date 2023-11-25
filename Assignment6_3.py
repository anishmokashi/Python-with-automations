''' write a program which contains one class named as Numbers.
Arithmetic class contains one instance variable as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There are four instance methods inside class as chkPrime(),Chkperfect(),Sumfactors(),Factors().
Chkprime() method will return true if number is prime otherwise return false.
ChkPerfect() method will return true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
Sumfactors() method will return addition of all factors.Use this method in any another method as a helper method if required.
After designing the above class call all instance methods by creating multiple objects.
Input : 11      Output : Number is prime number
Input : 28      Output : Number is perfect number
'''
class Numbers:
    def __init__(self,num):
        self.value=num 
    def ChkPrime(self):
        num=self.value
        for i in range(2,int((num/2)+1)):
             if(num%i==0):
                 return False
        else:
            return True
    def Factors(self):
        num=self.value
        factors=0
        for i in range(1,num):
            if(num%i==0):
                factors=factors+i
        return factors
    
    def ChkPerfect(self):
        '''Perfect number is a number which is equal to the sum of its factors
        '''
        num=self.value
        factors=self.Factors()
        if(factors==num):
            return True
        else:
            return False
def main():
    num=int(input("Enter a number to check if it is prime or perfect "))
    Obj1=Numbers(num)
    if(Obj1.ChkPrime()==True):
        print("Number is prime number")
    elif(Obj1.ChkPerfect()==True):
        print("Number is perfect number")
if __name__=="__main__":
    main()
    
    