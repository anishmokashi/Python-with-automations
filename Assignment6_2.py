'''Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount.
That class contains one class variable as ROI which is initialised to 10.5.
Inside init method initialise all name and amount variables by accepting the values from user.
There are four instance methods inside class as Display(),Deposit,Withdraw(),CalculateInterest().
Deposit() method will accept the amount from user and add that value in class instance variable Amount.
Withdraw() method will accept amount froom user and add that value in class instance variable Amount.
CalculateInterest() method calculate the interest based on Amount by considering rate of interest which is class variable as ROI.
And Display() method will display value of all the instance variables as Name Amount.
After designing the above class call all instance methods by creating multiple objects.
'''
class BankAccount:
    ROI=10.5
    def __init__(self,var1,var2):
        self.Name=var1
        self.Amount=var2
    def Display(self):
        print("Name ",self.Name)
        print("Current Balence is ",self.Amount)
    def Deposit(self):
        num=int(input("Enter how much amount you want to deposit "))
        self.Amount=self.Amount+num
        print(num," Deposited successfully")
    def Withdraw(self):
        num=int(input("Enter how much amount you want to Withdraw "))
        self.Amount=self.Amount-num
        print(num," Withdrawn successfully")
    def CalculateInterest(self):
        print("As per your account balance after considering rate of interest will be ",self.Amount*BankAccount.ROI)

def main():
    Obj1=BankAccount("Anish",5000)
    print("Welcome")
    Obj1.Display()
    Obj1.Deposit()
    Obj1.Display()
    Obj1.Withdraw()
    Obj1.Display()
    Obj1.CalculateInterest()
    print()
    print()

    Obj2=BankAccount("Sahil",7000)
    Obj2.Display()
    Obj2.Deposit()
    Obj2.Display()
    Obj2.Withdraw()
    Obj2.Display()
    Obj2.CalculateInterest()
if __name__=="__main__":
    main()